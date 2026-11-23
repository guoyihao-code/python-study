from 数据定义类 import ReaderContext
from 文件定义类 import FatherReader,NormalFile,JsonFile
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
text1=NormalFile(r"C:\Users\21062\Desktop\2013销售额.txt")
text2=JsonFile(r"C:\Users\21062\Desktop\2014销售额.txt")
data1=text1.reader_type()
data2=text2.reader_type()
all_data=data1+data2
data_dict={}
for key in all_data:
    if key.data in data_dict.keys():
        data_dict[key.data]+=key.money
    else:
        data_dict[key.data]=key.money


bar=Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title="柱状图")
)
bar.render("练习图表.html")
