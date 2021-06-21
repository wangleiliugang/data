d = dict(name='tarena', age=15)
print(d['age'])


d = {1:'one', 2:'two', 3:'三', 5:'five'}
for k, v in d.items():
    print('键是：', k, '值是：', v)

# 写程序，实现以下需求：
# 将如下数据形成一个字典seasons
# '键'　　　　　　　    　　　'值'
#  1           '春季有1，2，3月'
#  2           '夏季有4，5，6月'
#  3           '秋季有7，8，9月'
#  4           '冬季有10，11，12月'
# 让用户输入一个整数代表这个季度，打印这个季度的信息，如果用户输入的信息不存在字典的键内，则打印不存在

d = {1:'春季有1，2，3月', 
     2:'夏季有4，5，6月', 
     3:'秋季有7，8，9月', 
     4:'冬季有10，11，12月'
    }
# 方法1
n = int(input('请输入一个季度：'))
x = d.get(n, '不存在，您的输入有误！')
print(x)
# 方法2
n = int(input('请输入一个季度：'))
if n in d:
    print(d[n])
else:
    print('不存在，您的输入有误！')


# 写程序，输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数
# 如：输入　ABCDABCABA
# 　　　输出　 A: 4次
#         B: 3次
#         C: 2次
#         D: 1次
# 注：不要求打印的顺序
# 方法1(速度最快！)
s = input('请输入一段字符串：')
d = {}                       # 字典的键：出现的字符，字典的值：出现的次数
for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
print(d)
for k in d:
    print(k, ':', d[k], '次')

# 方法2
s = input('请输入一段字符串：')
s1 = ''
for ch in s:
    if ch not in s1:
        s1 += ch
print(s1)

for ch in s1:
    print(ch, ':', s.count(ch), '次')

# 练习
# 有字符串列表：L = ['tarena', 'xiaozhang', 'xiaowang']
# 生成如下字典：d = {'tarena': 6, 'xiaozhang': 9, 'xiaowang': 8}  注：字典的值是键的长度

L = ['tarena', 'xiaozhang', 'xiaowang']
d = {x : len(x) for x in L}
print(d)

# 编写列表如下：Nos = [1001, 1002, 1003, 1004]     names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 生成用Nos 数据为键，以names 为值的字典

Nos = [1001, 1002, 1003, 1004]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 方法1
d = {Nos[i] : names[i] for i in range(min(len(Nos), len(names)))}
print(d)
# 方法2
d = {x : names[Nos.index(x)] for x in Nos}
print(d)


























