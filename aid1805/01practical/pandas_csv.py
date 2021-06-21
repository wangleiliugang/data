import pandas as pd


# 1.to_string()用于返回DataFrame类型数据，如果不使用该函数，则输出结果为数据的前5行和末尾5行，中间部分以...代替。

df = pd.read_csv('nba.csv')
# print(df.to_string())
# print(df)
# 1.1head(n)方法用于读取前n行，如果不写n，默认返回5行
print(df.head(10))
# 1.2tail(n)方法用于读取尾部n行，如果不写n，默认返回5行，空行各个字段的值返回NaN。
print(df.tail(5))
# 1.3info()方法返回表格的一些基本信息
print(df.info())


# 2.可以使用to_csv()方法将DataFrame存储为csv文件。
# name = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wiki.com"]
# ag = [90, 40, 80, 98]
# dict = {'name': name, 'site': st, 'age': ag}
# df1 = pd.DataFrame(dict)
# df1.to_csv("site.csv")
