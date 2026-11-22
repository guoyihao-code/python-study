# 1. 找出最大值和最小值（自己写循环）
# nums = [5, 2, 9, 1, 7]
# maxNum=-1
# minNum=10000
# for i in nums:
#     if i>maxNum:
#         maxNum=i
#     if i<minNum:
#         minNum=i
# print(maxNum,minNum)
# print(max(nums),min(nums))
# 2. 每个元素乘 2，生成新列表（原列表不变）
# nums = [3, 6, 1, 8]
# new_list=[]
# for i in nums :
#     i*=2
#     new_list.append(i)
# print(nums)
# print(new_list)
# 3. 删除列表中所有的偶数
# nums = [1, 4, 6, 7, 8, 9, 10]
# new_list=[]
# for i in nums:
#     if i%2==0:
#         continue
#     new_list.append(i)
# print(new_list)
# 4. 合并两个列表、去重、从小到大排序（这题可以用 sorted）
# a = [3, 1, 4]
# b = [1, 5, 9]
# c=a+b
# d=list(set(c))
# print(sorted(d))
# 5. 二维列表所有元素求和（两层循环）
# grid = [[1, 2, 3], [4, 5], [6]]
# total=0
# for i in grid:
#     for j in i:
#         total+=j
# print(total)



# 1. 只用 insert 和 extend，把 a 变成 [0, 1, 2, 3, 4, 5]
# a=[1,2,3]
# a.insert(0,0)
# a.extend([4,5])
# print(a)
# 2. 统计每个元素出现次数（用 list.count，不要用字典）
# nums = [1, 2, 2, 3, 3, 3]
# unique=[]
# for num in nums:
#     if num not in unique:
#         unique.append(num)
# for i in unique:
#     print(i,"出现",nums.count(i),'次')
# 3. 原地删除所有值为 2 的元素（用倒序循环，不许生成新列表）
# nums = [1, 2, 2, 3, 2, 4]
# for i in range(len(nums)-1,-1,-1):
#     if nums[i]==2:
#         del nums[i]
# print(nums)
# 4. 建一个 3×3 的全 0 矩阵，把第 2 行第 2 列改成 9，打印出来
#    预期：
#    [[0, 0, 0], [0, 9, 0], [0, 0, 0]]
# my_list=[[0,0,0],[0,0,0],[0,0,0]]
# my_list[1][1]=9
# print(my_list)
# 5. 转置矩阵（行变列）
m = [[1, 2, 3], [4, 5, 6]]
# 预期：[[1, 4], [2, 5], [3, 6]]


