#集合set，定义，插入，删除，交集，并集，
a={1,3,5,6,7,8,9}
a.add(10)
print(a)
#discard()删除不存在的元素不会报错，remove会keyError
a.remove(1)
a.discard(3)
print(a)
#pop()随机删除一个元素
a.pop()
print(a)
b={1,3,4,5,6,89,67}
print(a|b)
print(a&b)
print(a-b)
print()
#集合1.difference_update(集合2）在集合1中删除与集合2相同的元素，集合2不改变
a.difference_update(b)
print(a)
print(b)
print()
#两个集合合并 集合1.union(集合2）
c=a.union(b)
print(c)
print()



#集合的常见应用
#1,列表list去重
a=[1,1,2,3,2,3,4,5,6]
a=list(set(a))
print(a)


#2判断有无重复
a=[1,2,9,7,2,3,4]
if len(a)!=len(set(a)):
    print("有重复")
else:
    print("没有重复")

#3快速查找
a={1,2,3,4,5}
b=int(input())
while True:
    if b in a:
        print("禁止使用,重新输入")
        b=int(input())
    else:
        a.add(b)
        print(f"新的a集合为{a}")
        break