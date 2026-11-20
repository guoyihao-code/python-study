# 1. 列表去重（用 set）
# nums = [1, 2, 2, 3, 3, 3, 4]
# new_list=list(set(nums))
# print(new_list)
# 2. 求交集、并集、差集（a 有 b 没有）
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a&b)
# print(a|b)
# print(a-b)
# 3. 找出 "hello world" 里所有不重复的字母，排序后打印
#    预期：[' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w']
# my_str="hello world"
# s=set(my_str)
# res=sorted(s)
# print(res)
# 4. 判断两个列表有没有共同元素（用集合，不要双层循环）
# x = [1, 5, 9]
# y = [2, 5, 7]
# common=set(x)&set(y)
# if common:
#     print("yes")
# else:
#     print("no")
# 5. 统计一段文本里"不同的单词"有多少个（split + set）
text = "the cat and the dog and the bird"
my_list=text.split(" ")
my_list2=list(set(my_list))
print(len(my_list2))