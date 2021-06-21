import re


pattern = r'\w+'

# 获取正则表达对象
obj = re.compile(pattern)

lst = obj.findall('hello world')
print(lst)
