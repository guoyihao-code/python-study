my_str="Hello Word"
print(my_str.index('e'))
New_str=my_str.replace("Word","guo")
print(New_str)

my_list=[1,2,3,4,5,6]
my_list.insert(0,100)#无返回值，会返回None
print(my_list)
my_list.extend([1,2,3,45,6])#同样无返回值
print(my_list)

sentence="the cat and the dog and the bird"
words=sentence.split(" ")
my_dict={}
for word in words:
    my_dict[word]=my_dict.get(word,0)+1

students = {
    "张三": {"语文": 90, "数学": 88},
    "李四": {"语文": 75, "数学": 92},
}
name=input("请输入姓名")
subject=input("科目")
print(students[name][subject])