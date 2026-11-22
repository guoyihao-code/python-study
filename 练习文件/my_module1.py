__all__=["add"]
def add(a,b):
    print(a+b)
def add2(a,b):
    print(a+b+a+b)
if __name__ == '__main__':
    add(3,7)
#如果一个模块有--all--变量，使用from x import*只会调用all内容里面