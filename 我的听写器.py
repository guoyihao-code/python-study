import random
def load_word(path="data/words.csv"):
    words=[]
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(",")
            if len(parts)!=2:
                continue
            en=parts[0]
            ch=parts[1]
            words.append((en,ch))
    return words
def quiz(words,n):
    score=0
    picks=random.sample(words,n)
    for i in range(len(picks)):
        #en,ch=random.choice(words)
        en,ch=picks[i]
        answer=input(f"第{i+1}题,{ch}的英文是")
        if answer.strip().lower()==en.lower():
            print("回答正确")
            score+=1
        else:
            print(f"回答错误，答案是{en}")
            save_wrong(en)
    return score,len(picks)
def save_wrong(en):
    with open("data/wrong.txt","a",encoding="utf-8") as f:
        f.write(en+"\n")
def load_wrong(path="data/wrong.txt"):
    wrong=[]
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line:
                wrong.append(line)
    return wrong
words=load_word()
score,total=quiz(words,10)
wrong=load_wrong()
print(f"共得{score}/{total}分")
print(f"错词共有{len(wrong)}个")
