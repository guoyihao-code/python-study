#统计每个单词出现的次数
sentence="the cat and the dog and the bird"
words=sentence.split()
cnt_dict={}
for word in words:
    # if word in cnt_dict:
    #     cnt_dict[word]+=1
    # else:
    #     cnt_dict[word]=1
    cnt_dict[word]=cnt_dict.get(word,0)+1
print(cnt_dict)
#合并两个字典
d1={"a":1,"b":2}
d2={"c":9,"d":3}
d1.update(d2)
d3={**d1,**d2}
print(d1)
print(d3)
#找出成绩最高的人
scores={"张三":90,"李四":85,"王五":92}
maxScore=0
name="none"
for key in scores:
    if scores[key]>maxScore:
        maxScore=scores[key]
        name=key
print(f"最高分是{name}为{maxScore}")
#查询
students = {
    "张三": {"语文": 90, "数学": 88},
    "李四": {"语文": 75, "数学": 92},
}
name=input("你要查询的人")
subject=input("科目")
if name in students:
    if subject in students[name]:
        print(students[name][subject])
    else:
        print("没有此科目")
else:
    print("没有此人")

