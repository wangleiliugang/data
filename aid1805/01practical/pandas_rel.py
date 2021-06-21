import pandas as pd


# 1.简单的实例
mydataset = {
    'sites': ["Google", "Runoob", "Wiki"],
    'number': [1, 2, 3],
}

myvar = pd.DataFrame(mydataset)
print(myvar)


# 2.以下示例pandas数据结构-Series
# pandas.Series(data, index, dtype, name, copy)
# 参数说明：
# data:一组数据(ndarray类型)
# index:数据索引标签，如果不指定，默认从0开始
# dtype:数据类型，默认会自己判断
# name:设置名称
# copy:拷贝数据，默认为False

# 2.1没有指定索引，索引值就从0开始，并可以根据索引值读取数据
# a = [1, 2, 3]
# myvar1 = pd.Series(a)
# print(myvar1)
# print(myvar1[1])

# 2.2可以人为指定索引值，并可以根据索引值读取数据
# b = ["Google", "Runoob", "Wiki"]
# myvar2 = pd.Series(b, index=["X", "Y", "Z"])
# print(myvar2)
# print(myvar2["Y"])

# 2.3可以使用key/value对象，类似字典来创建Series --> 字典的key变成了索引值
# sites1 = {1: "Google", 2: "Runoob", 3: "Wiki"}
# myvar3 = pd.Series(sites1)
# print(myvar3)

# 2.4如果只需要字典的一部分数据，只需要指定需要数据的索引即可
# sites2 = {1: "Google", 2: "Runoob", 3: "Wiki"}
# myvar4 = pd.Series(sites2, index=[1, 2])
# print(myvar4)

# 2.5设置Series名称参数
sites3 = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar5 = pd.Series(sites3, index=[1, 2], name="runoob-Series-Test")
print(myvar5)


# 3.以下示例pandas数据结构-DataFrame
# pandas.DataFrame(data, index, columns, dtype, copy)
# 参数说明:
# data:一组数据(ndarray, series, map, lists, dict等类型)
# index:索引值，或者可以称为行标签
# columns:列标签，默认为Rangelndex(0,1,2,...n)
# dtype:数据类型
# copy:拷贝数据，默认为False

# 3.1pandas.DataFrame是一个二维的数组结构，类似二维数组
# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=float)
# print(df)

# 3.2以下使用ndarrays创建，ndarray的长度必须相同，如果传递了index，则索引的长度应等于数组的长度；如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。
# data1 = {
#     'Site': ["Google", "Runoob", "Wiki"],
#     'Age': [1, 2, 3],
# }
# df1 = pd.DataFrame(data1)
# print(df1)

# 3.3可以使用字典(key/value)，其中字典的key为列名；没有对应的部分数据为NaN
# data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# df2 = pd.DataFrame(data2)
# print(df2)

# 3.4pandas可以使用loc属性返回指定行的数据，如果没有设置索引，第一行索引为0，第二行索引为1，以此类推。
# 注意：返回结果其实就是一个pandas Series数据；
# data3 = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
# df3 = pd.DataFrame(data3)
# print(df3.loc[0])
# print(df3.loc[1])

# 3.5也可以返回多行数据，使用[[XX]]格式，XX为各行的索引，以逗号隔开。
# 注意：返回结果其实就是一个pandas DataFrame数据；
# data4 = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
# df4 = pd.DataFrame(data4)
# print(df4.loc[[0, 1]])

# 3.6可以指定索引值；可以使用loc属性返回指定索引对应到某一行。
data5 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df5 = pd.DataFrame(data5, index=["day01", "day02", "day03"])
print(df5)
print(df5.loc["day02"])
