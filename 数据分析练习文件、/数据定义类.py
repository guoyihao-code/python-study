#定义数据中的排序对象
class ReaderContext:
    def __init__(self,data,money):
        self.data=data
        self.money=money
    def __str__(self) -> str:
        return f"{self.data},{self.money}"





