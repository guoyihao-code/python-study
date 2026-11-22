# class Students:
#     name=None
#     age=None
#     def say_hi(self):
#         print(f"你们好，我是{self.name}，今年{self.age}岁")
# stu1=Students()
# stu1.name="郭毅豪"
# stu1.age=18
# stu1.say_hi()
#构造方法,魔术方法
class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print(f"Student类创建了一个类对象")
    def __str__(self)->str:
        return f"hello my name is {self.name}"
    def __lt__(self, other):#le 用于>=或<=
        return self.age<other.age
    def __eq__(self, other):
        return self.age==other.age
stu1=Student("郭毅豪",18,110)
stu2=Student("贾俊哲",18,120)
print(stu1)
print(stu1<stu2)
print(stu1==stu2)



