import pandas as pd


# 1.to_string()用于返回DataFrame类型数据，也可以直接处理JSON字符串。
# df = pd.read_json("sites.json")
# print(df.to_string())

# 2.JSON对象与python字典具有相同的格式，故可以将python字典转换为DataFrame数据
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "google", "row2": "baidu", "row3": "taobao"}
}
df1 = pd.DataFrame(s)
print(df1)

# 3.从url中读取JSON数据
# URL = "https://static.runoob.com/download/sites.json"
# df2 = pd.read_json(URL)
# print(df2)

