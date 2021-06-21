import re

re_obj = re.compile('(ab)cd(?P<dog>ef)')
match_obj = re_obj.search('hi, dsabcdefghijk')

print('search:', match_obj.group())

# match对象属性
print('re:', match_obj.re)  # 使用的正则表达式
print('pos:', match_obj.pos)  # 匹配目标字符串的开始位置
print('endpos:', match_obj.endpos)  # 匹配目标字符串的结束位置
print('lastgroup:', match_obj.lastgroup)  # 获取最后一组的名称；如果无名字则返回None
print('lastindex:', match_obj.lastindex)  # 最后一组是第几组
print('*' * 30)

# match obj属性函数
print('start():', match_obj.start())  # 获取匹配内容在字符串中的开始位置
print('end():', match_obj.end())  # 获取匹配内容在字符串中的结束位置(结束位置的下一位)
print('span():', match_obj.span())  # 获取匹配内容在字符串中的起止位置
print('group():', match_obj.group())  # 获取match_obj对象匹配的内容
print('group(1):', match_obj.group(1))  # 获取第1个子组的匹配内容
print('group(2):', match_obj.group(2))  # 获取第2个子组的匹配内容
print('groups():', match_obj.groups())  # 返回值是元组，获取所有子组中的内容
print('groupdict():', match_obj.groupdict())  # 返回所有捕获组构成的字典
