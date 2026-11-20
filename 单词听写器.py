import json
import os
import random

WRONG_FILE = "data/wrong.json"
def load_word(path="data/words.csv"):
    """读词库，返回 [(英文, 中文), ...]"""
    words = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            en = parts[0].strip()
            zh = parts[1].strip()
            words.append((en, zh))
    return words
def load_wrong():
    """读错词本：文件不存在就当空的"""
    if not os.path.exists(WRONG_FILE):
        return {}
    with open(WRONG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save_wrong(wrong):
    """存错词本"""
    with open(WRONG_FILE, "w", encoding="utf-8") as f:
        json.dump(wrong, f, ensure_ascii=False, indent=2)
def quiz(words, wrong, n=10):
    """错词优先 + 补充新词；返回 (得分, 本轮题目, 答错的词)"""
    zh_of = {en: zh for en, zh in words}
    # ① 先把错词本里还在词库中的词挑出来，最多占一半
    review = [en for en in wrong if en in zh_of]
    random.shuffle(review)
    picks = review[: min(len(review), n // 2)]
    # ② 剩下的名额从没抽到的词里补
    pool = [en for en, _ in words if en not in picks]
    need = n - len(picks)
    picks += random.sample(pool, min(need, len(pool)))
    random.shuffle(picks)

    score = 0
    missed = []

    for i, en in enumerate(picks, start=1):
        zh = zh_of[en]
        ans = input(f"[{i}/{len(picks)}] {zh} -> ")
        if ans.strip().lower() == en.lower():
            print("  ✓ 对")
            score += 1
            if en in wrong:                  # 复习答对：错次减一，减到 0 就移出
                wrong[en] -= 1
                if wrong[en] <= 0:
                    del wrong[en]
        else:
            print(f"  ✗ 错，正确答案：{en}")
            wrong[en] = wrong.get(en, 0) + 1
            missed.append(en)

    return score, picks, missed


def show_result(score, total, missed, wrong):
    if total == 0:
        print("词库是空的，检查 data/words.csv")
        return
    print()
    print("=" * 32)
    print(f"得分：{score}/{total}  ({score / total * 100:.0f}%)")
    if missed:
        print("这轮错的词：")
        for en in missed:
            print(f"  {en}")
    else:
        print("全对，漂亮。")
    print(f"错词本累计 {len(wrong)} 个词（下次会优先考它们）")


if __name__ == "__main__":
    words = load_word()
    wrong = load_wrong()

    score, picks, missed = quiz(words, wrong, 10)
    save_wrong(wrong)
    show_result(score, len(picks), missed, wrong)
