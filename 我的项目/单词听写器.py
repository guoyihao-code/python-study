import json
import random
path1=r"C:\Users\21062\PycharmProjects\PythonProject1\data\words.csv"
path2=r"C:\Users\21062\PycharmProjects\PythonProject1\data\wrong.json"

def word_list(path):
    pairs=[]
    with open(path,'r',encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(",")
            if len(parts)!=2:
                continue
            pairs.append((parts[1],parts[0]))
    return pairs


def count_word(path):
    try:
        with open(path,'r',encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return{}


def add_word(word,counts):
    counts[word]=counts.get(word,0)+1
    return counts[word]      #返回的是错误的次数


def rewrite_file(path,counts):
    with open(path, 'w',encoding="utf-8")as f:
        json.dump(counts,f,ensure_ascii=False,indent=2)


def pick_word(words,counts,n):
    heavy=[]
    light=[]
    for c,e in words:
        if e in counts:
            heavy.append((c,e))
        else:
            light.append((c,e))
    random.shuffle(heavy)
    random.shuffle(light)
    return heavy[:3]+light[:2]

def main():
    words=word_list(path1)
    counts=count_word(path2)
    test=pick_word(words,counts,5)
    print(f"词库 {len(words)} 个词，历史错词 {len(counts)} 个\n")
    right=0
    for c ,e in test:
        answer=input(f"{c}的英文为").strip()
        if answer.lower()==e.lower():
            print("回答正确")
            right+=1
        else:
            times=add_word(e,counts)
            print(f"回答错误，正确答案{e},你已错误{times}次")
    print(f"测试完毕，你答对{right}道题")
    rewrite_file(path2,counts)
if __name__=="__main__":
    main()













