class FileText:
    def __init__(self,data,money):
        self.data=data
        self.money=money
    def __str__(self):
        return f"{self.data},{self.money}"
