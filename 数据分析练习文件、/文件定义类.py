#两份文件有一份json文件
import json
from 数据定义类 import ReaderContext
class FatherReader:
    def reader_type(self):
        pass
class NormalFile(FatherReader):
    def __init__(self,path):
        self.path=path
    def reader_type(self):
        res_list=[]
        with open(self.path,'r',encoding="utf-8") as f:
            for line in f:
                line =line.strip()
                temp_list=line.split(",")
                temp=ReaderContext(temp_list[0],temp_list[1])
                res_list.append(temp)
        return res_list

class JsonFile(FatherReader):
    def __init__(self,path):
        self.path=path
    def reader_type(self):
        res_list=[]
        with open(self.path,'r',encoding="utf-8") as f:
            for line in f:
                temp_list=json.loads(line)
                temp=ReaderContext(temp_list["日期"],temp_list["销售额"])
                res_list.append(temp)
        return res_list
