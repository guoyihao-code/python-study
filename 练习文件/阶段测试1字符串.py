# 1. 把 "hello world" 变成 "Hello World"
# s = "hello world"
# new_str=s.strip()
# print(new_str.title())
# 2. 去掉两端空白，并打印"去掉前"和"去掉后"的长度
# s = "   Python 真好用  "
# new_str=s.strip()
# print(len(s),len(new_str))
# 3. 把 "2026-11-08" 拆成 年 / 月 / 日 三个变量并打印
# s = "2026-11-08"
# list=s.split("-")
# print(list[0],list[1],list[2])
# 4. 把列表拼成字符串 "我爱学py"
#parts = ["我", "爱", "学", "py"]
# my_str="".join(parts)
# print(my_str)
# str=""
# for i in parts:
#     str+=i
# print(str)
# 5. 统计 "Hello World 123" 里大写、小写、数字各几个
s = "Hello World 123"
# 预期：大写 2，小写 8，数字 3
dx=0
xx=0
sz=0
for ch in s:
    if ch.isupper():
        dx+=1
    elif ch.islower():
        xx+=1
    elif ch.isdigit():
        sz+=1
    else:
        continue
print(dx,xx,sz)
