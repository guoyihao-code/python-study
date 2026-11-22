from pyecharts.charts import Bar
from pyecharts import options as opts
bar=(
    Bar()
    .add_xaxis(["语文", "数学", "英语"])
    .add_yaxis("张三", [90, 85, 78])
    .add_yaxis("李四", [88, 92, 70])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="成绩对比"),
        xaxis_opts=opts.AxisOpts(name="科目"),
        yaxis_opts=opts.AxisOpts(name="分数"),
    )
)
bar.render("成绩对比.html")
print("已生成 成绩对比.html")