import re

pattern = r'((?P<word>ab)cd(?P<test>ef))'
# 获取正则表达对象
obj = re.compile(pattern)

# 匹配目标字符串＝回去返回值列表
lst = obj.findall('abcdefabcdefabefhsg')
print(lst)

# 以一个或者多个空字符切割字符串
l1 = re.split(r'\s+', 'hello world nihao   china')
print(l1)

# 将目标字符串大写字母替换为##
s1 = re.sub(r'[A-Z]', '##', 'Hi,Jame.It is a fun day', 2)
print(s1)

# 返回值多一个实际替换的个数
s2 = re.subn(r'[A-Z]', '$$', 'Hi,Jame.It is a fun day')
print(s2)

print(obj.groupindex)
print(obj.groups)
