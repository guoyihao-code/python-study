# 1. 写 add(a, b) 返回两数之和，然后调用打印结果
#    要求：函数里用 return，不要用 print
# def add(a,b):
#     return a+b
# res=add(5,3)
#print(res)
#print(add(5,3))
# 2. 写 is_even(n)，偶数返回 True，奇数返回 False
#    （上次这道你写成了 n & 2 == 0）
# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(even(7))
# 3. 写 count_vowels(s)，统计字符串里元音字母（aeiou）个数
#    count_vowels("hello world")  → 3
# def count_vowels(s):
#     cnt=0
#     vowels="aeiou"
#     for i in s:
#         if i in vowels:
#           cnt+=1
#     return cnt
# print(count_vowels("hello word"))
# 4. 写 find_max(nums)，返回列表最大值，函数里不许用 max()
#    写完用 [3, 9, 2, 7] 和 [-5, -2, -9] 各测一次
def find_max(nums):
    max_num=nums[0]
    for i in nums:
        if i>max_num:
            max_num=i
    return max_num
list1=[3,9,2,7]
list2=[-5,-2,-9]
print(find_max(list1),find_max(list2))
