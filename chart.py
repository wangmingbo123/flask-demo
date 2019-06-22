from pyecharts.charts import Bar
from example.commons import Faker

bar = Bar()

list = ["a", "s", "d"]
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_xaxis(list)
bar.add_yaxis("商家A", [5, 20, 36])
bar.add_yaxis("商家B", [6, 10, 16])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()


print(Faker.choose())
