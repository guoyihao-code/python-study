# try:
#     f=open("D:/abc.txt","r",encoding="utf-8")
# except:
#     f=open("D:/abc.txt","w",encoding="utf-8")
# try:
#     print(name)
# except NameError as a:
#     print("变量未定义")
#     print(a)
# try:
#     print(name)
#     print(1/0)
# except (ZeroDivisionError,NameError) as e:
#     print("错误")
#     print(e)
try:
    print(3)
except Exception as e:
    print("出现异常")
    print(e)
else:
    print("没有异常")



