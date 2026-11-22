#1设计一个类，完成对数据的封装
#2设计一个抽象类，定义文件读取的相关功能，并使用子类文件实现具体的功能
#3读取文件，生成数据对象
#4进行数据需求的逻辑计算
#5pyecharts进行绘图

from pyecharts.charts import Bar          #构建柱状图对象
from pyecharts.options import *           #构建可选选项
from pyecharts.globals import ThemeType   #构建主题，颜色等
from file_define import FileReader, TextFileReader,JsonFileReader
from data_define import Record
text1=TextFileReader(r"C:\Users\21062\Desktop\2011销售额.txt")
text2=JsonFileReader(r"C:\Users\21062\Desktop\2012销售额.txt")
data1:list[Record]=text1.read_data()
data2:list[Record]=text2.read_data()
#将两个数据合并
all_data:list[Record]=data1+data2

data_dict={}
for record in all_data:
    if record.data in data_dict.keys():
        data_dict[record.data]+=record.money
    else:
        data_dict[record.data]=record.money
print(data_dict)

#可视化图标开发
bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))   #注意要将key转换成list
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每年月份销售额")
)
bar.render("销售额柱状图.html")

