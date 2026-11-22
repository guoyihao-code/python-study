#数据定义的类
class Record:
    def __init__(self,date,order_id,money,province):
        self.data=date
        self.order_id=order_id
        self.money=money
        self.province=province

    def __str__(self) -> str:
        return f"{self.data},{self.order_id},{self.money},{self.province}"
