#1先定义一个抽象类用来做顶层设计，确定有那些功能需要实现
import json
from data_define import Record

class FileReader:
    def read_data(self)->list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path=path

    def read_data(self)->list[Record]:
        my_list=[]
        f=open(self.path,"r",encoding="utf-8")
        for line in f.readlines():
            line=line.strip()#消除\n
            data_list=line.split(",")
            record=Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            my_list.append(record)
        f.close()
        return my_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path=path

    def read_data(self) -> list[Record]:
        my_list = []
        f = open(self.path, "r", encoding="utf-8")
        for line in f.readlines():
             data_dict= json.loads(line)
             record=Record(data_dict["日期"],data_dict["订单ID"],data_dict["销售额"],data_dict["地点"])
             my_list.append(record)
        f.close()
        return my_list






if __name__=="__main__":
  Text_file=TextFileReader(r"C:\Users\21062\Desktop\2011销售额.txt")
  Json_file=JsonFileReader(r"C:\Users\21062\Desktop\2012销售额.txt")
  list1=Text_file.read_data()
  list2=Json_file.read_data()
  for l in list1:
      print(l)
  for l in list2:
      print(l)
