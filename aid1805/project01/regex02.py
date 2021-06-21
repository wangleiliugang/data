import re

obj = re.compile(r'foo')

iter_obj = obj.finditer('foo,food on the table')
for i in iter_obj:
    # print(i)
    # print(dir(i))
    print(i.group())

# match 只能匹配开头
try:
    m_obj = obj.match('foo,food on the table')
    # m_obj = obj.match('Foo,food on the table')
    print(m_obj.group())
except AttributeError:
    print("match none")

# search 可以匹配任意位置，但只能匹配一处
try:
    m_obj = obj.search('Foo,food on the table')
    print(m_obj.group())
except AttributeError:
    print("match none")
