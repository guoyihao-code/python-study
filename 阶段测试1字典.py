# 1. 统计字符串里每个字符出现的次数（用 get）
# s = "hello"
# d={}
# for ch in s:
#     d[ch]=d.get(ch,0)+1
# print(d)
# 2. 遍历字典，打印 "键: 值"
d = {"语文": 90, "数学": 85, "英语": 78}
# for key in d:
#     print(key,d[key])
# for key,value in d.items():
#     print(key,value)
# for v in d.values():
#     print(v)
# 3. 找出分数最高的科目和分数
# d = {"语文": 90, "数学": 85, "英语": 95}
# max_subject=""
# max_score=-1
# for k,v in d.items():
#     if v>max_score:
#         max_score=v
#         max_subject=k
# print(max_subject,max_score)
# max_k=max(d,key=d.get)
# print(max_k,d[max_k])
# 4. 合并两个字典（有重复键时，后面的覆盖前面的）
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 99, "c": 3}
# d3=d1|d2
# print(d3)
# 5. 嵌套字典：查"张三"的"数学"成绩
students = {
    "张三": {"语文": 90, "数学": 85},
    "李四": {"语文": 88, "数学": 92},
}
print(students["张三"]["数学"])



