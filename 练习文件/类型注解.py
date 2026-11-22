#1变量类型注解  :类型=
age:int=18
#2基础容器的注解
my_list:list=[1,'hao',3]
my_new_list:list[int]=[1,2,3]
my_tuple:tuple=(1,'yi',3)
my_set:set={1,'guo',3}
my_str:str="guo yi hao"
#3 注释#type:int
my_new_new_list=[1,2,3,5,4] # type:list[int]
#4函数形参类型注解,返回值注解.
def add(x:int, y:int)->int:
    return x+y
res=add(2,1)
print(res)
#5union类型注解，混合类型
from typing import Union
my_list2:list[Union[int,str]]=[1,2,3,"guo yi hao"]



