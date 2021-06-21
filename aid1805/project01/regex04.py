import re


# 1.匹配时忽略大小写
re_obj = re.compile('abcd', re.I)
lst = re_obj.findall('hi, abcd, ABcd, ABCD')
print(lst)

# 2.匹配换行，对.元字符起作用
s = '''hello world
 nihao china
'''
# l1 = re.findall('.*', s, re.S)
l1 = re.findall('.+', s, re.S)
print(l1)

# 3.开头结尾计算换行，对^ $起作用
obj = re.search('^\snihao', s, re.M)
# obj = re.search('world$', ss, re.M)
print(obj.group())
print('***************************')


# 4.让正则表达式能以#添加注释
re_obj = re.compile(
    '''(ab)#This is group1
    cd
    (?P<dog>ef) #This is group dog''', re.X)
print(re_obj.search('abcdefghijk').group())
