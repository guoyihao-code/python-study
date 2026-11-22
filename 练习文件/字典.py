#字典dict,不可重复{key:value,},字典[key]可以取到对应的value
my_dict1={"guo":100,"wang":69,"zhou":90}
my_dict2={}
my_dict3=dict()
print(type(my_dict1))
print(my_dict1["guo"])
#字典的嵌套
student={
    "xiaoming":{
        "yuwen":77,"shuxue":89
    },
    "xiaoguo":{
        "yuwen":100,"shuxue":100
    },
    "xiaojia":{
        "yuwen":100,"shuxue":89
    }
}
print(student)
print(student["xiaoguo"]["shuxue"])


#字典的常用操作
#修改字典 字典[key]=value
student["xiaojia"]["yuwen"]=99
print(student["xiaojia"]["yuwen"])
#删除元素
student.pop("xiaoming")
print(student)
#清空字典clear
#获得全部的key,字典.keys()
keys=student.keys()
print(keys)
#遍历字典
for i in keys:
    print(f"{i},{student[i]}")
for i in student:
    print(f"{i},{student[i]}")
#统计元素的数量
print(len(student))
