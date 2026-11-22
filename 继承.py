#单继承
class Student:
    name="xiao jia"
    age=18
    def say_hi(self):
        print(f"你们好我是{self.name},我今年{self.age}岁")
class NewStudent(Student):
    other_name="xiao guo"
    def say_true(self):
        print(f"{self.name}没有{self.other_name}帅")
stu1=NewStudent()
stu1.say_true()
class Teacher(NewStudent):
    def say(self):
        print(f"{self.name},{self.other_name}都是我的学生")
teacher=Teacher()
teacher.say()
#多继承一样，传参多几个，不写了
#2复写直接在子类对变量从新赋值
#3修改后调用父类成员-1父类名.成员变量,-2super().成员变量/成员方法
