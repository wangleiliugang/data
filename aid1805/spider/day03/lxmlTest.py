from lxml import etree


def info(object, spacing=20, collapse=0):
    """
    按照一定格式打印出模块及方法的详细意思
    """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print('\n'.join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList]))


xml = """
<note>
<person>
    <name lang="en">George</name>
    <age>25</age>
    <height>175</height>
</person>
<person>
    <name lang="chs">xiaoming</name>
    <age>31</age>
    <height>186</height>
</person>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>
"""
# print(xml)

# 1.得到根节点对象
root = etree.fromstring(xml)
print('根节点:', root)

# 2.返回一个列表，得到子节点对象及文本内容
elements = root.xpath('person')
print('子节点', elements)
print(elements[0])
print(elements[0].getchildren())
print(elements[0].getchildren()[0].text)
# info(elements[0])
# info(elements[0].getchildren()[0])


# 尝试用不关心节点结构的方法来获取到数据；在已匹配节点'person'后代中选取节点，不考虑目标节点的位置
# 提取属性信息
attributesElements = root.xpath("//@lang")
print(attributesElements)

# 提取节点信息
elements2 = root.xpath("/note/person[age<30]/name")
for i in elements2:
    print(i.text)

elements3 = root.xpath("/note/person/name[@lang='chs']")
for i in elements3:
    print(i.text)
