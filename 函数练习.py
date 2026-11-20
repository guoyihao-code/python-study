money=50000
name=input("请输入你的名字\n")
def query (show_header):
    if show_header:
         print("======查询页面======")
    print(f"{name},你的余额为{money}")
def saving (num):
    global money
    money+=num
    print(f"你已存入{num}元")
    query(False)
def get_money(num):
    global money
    money-=num
    print(f"你已取款{num}")
    query(False)
def main():
    print("=====主菜单=====")
    print(f"{name}你好")
    print("1查寻，2存钱，3取钱,4退出")
    return input("请输入")
while True:
    key_board=main()
    if key_board=="1":
        query(True)
        continue
    elif key_board=="2":
        num=int(input("输入存款金额"))
        saving(num)
        continue
    elif key_board=="3":
        num=int(input("请输入取款金额"))
        get_money(num)
        continue
    elif key_board=="4":
        print("退出")
        break
