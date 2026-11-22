str="guoyihaozhenshuai"
# 1，通过下表索引位置
print(str[2],str[0])

# 2，Index方法
print(str.index("g"))

# 3，replace 方法
newstr=str.replace("guo","haha")
print(newstr)

# 4，split split()去前后空格，split(" ")加空格
str="hello Word"
print(str.split(" "))

# 5，统计出现次数
str="guoyihao"
print(str.count("o"))
# 6，长度
print(len(str))
#7,删除
str="12guoyihao21"
print(str.strip("12"))
#字符串大小比较
print(f"a>b的比较结果是{"a">"b"}")