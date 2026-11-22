from 文件定义类 import FileText
import json
class Reader:
    def read_data(self):
        pass
class TextFile(Reader):
    def __init__(self,path):
        self.path=path
    def read_data(self)->list[FileText]:
        list_data=[]
        with open(self.path,"r",encoding="utf-8") as f:
            for line in f:
                line =line.strip()
                list1=line.strip("r")
                record=FileText(list1[0],list1[1])
                list_data.append(record)
class JsonFile(Reader):
    def __init__(self,path):
        self.path=path
    def read_data(self)->list[FileText]:
        list_data=[]
        with open(self.path,"r",encoding="utf-8") as f:
            for line in f:
                dict1=json.loads(line)
                record=FileText(dict1["日期"],dict1["销售额"])
                list_data.append(record)






