#1插入两个数字
# name=18
# high=180
# print("郭毅豪的年龄是：%d,\n身高是：%d" %(name,high))
# print(f"名字{name},身高{high}")
# num1=11
# num2=11.8954
# print("%d"%num1)
# print("%.3f"%num2)
# print("请输入你的名字")
# name=input()
# print("你的名字是：%s"%name)
# a,b=map(int,input().split())
# if a>89 :
#     print("你好老")
# else :
#     print("你好")
# age=int(input("请输入你的年龄\n"))
age,workage=map(int,input().split())
if ege>18:
    print("已成年")
    if workage>3:
        print("恭喜你，可以领取礼物")
    else:
        print("很遗憾，入职时长不够")
else:
    print("未成年")