# class Student:
#     __score=70
#     def __secret(self):
#         print(f"你的分数为{self.__score}")
#     def can_print(self):
#         if self.__score>=60:
#             print(f"你的成绩及格")
#         else:
#             print(f"你的成绩不及格")
# stu1=Student()
# stu1.can_print()
class Phone:
    __is_5g_enable=False
#提供私有的成员方法
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")
#提供公开的成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在使用")
phone=Phone()
phone.call_by_5g()

