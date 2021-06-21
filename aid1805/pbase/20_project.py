# 写一个程序，输入一些单词和解释，将单词作为键，将解释作为值，将这些数据存入字典中
# 然后：输入查找的单词，显示出此单词的解释

d = {}
while True:
    w = input('请输入单词(输入回车程序结束)：')
    if w == '':              # if not w:
        break
    e = input('请输入解释：')
    d[w] = e
print(d)
while True:
    n = input('请输入要查找的单词(输入回车程序结束)：')
    if not n:
        break
    print('单词的解释是：', d.get(n, "未找到这个单词！"))


# 学生管理项目准备工作：
# 写一个程序，任意输入n 个学生的信息，形成字典后存于列表中
# 学生的信息包括：姓名(字符串)，　年龄(整数)，　成绩(整数)
# 1)循环输入学生信息，直到输入学生姓名为空时结束输入，最后形成如下字典：
# L = [
#     {'name': 'xiaozhang','age': 20, 'score': 100},
#     {'name': 'xiaoli','age': 21, 'score': 97},
#     {'name': 'xiaowang','age': 19, 'score': 89},...
#     ]
# 2)将以上列表显示为如下的表格
#   +-------------+-------+---------+
#   |    name     |  age  |  score  | 
#   +-------------+-------+---------+
#   |   xiaoli    |  21   |   97    |
#   |  xiaozhang  |  20   |   100   |
#   |  xiaowang   |  19   |   89    |
#   +-------------+-------+---------+

# 1)解法
# 方法1
# L = []
# d = {}
# while True:
#     name = input('请输入学生姓名：')
#     if not name:
#         break
#     age = int(input('请输入年龄：'))
#     score = int(input('请输入成绩：'))
#     d['name'] = name
#     d['age'] = age
#     d['score'] = score

#     d1 = d.copy()
#     L.append(d1)
# print(L)

# 方法2
L = []
while True:
    name = input('请输入学生姓名：')
    if not name:
        break
    age = int(input('请输入年龄：'))
    score = int(input('请输入成绩：'))
    d = {}
    d['name'] = name
    d['age'] = age
    d['score'] = score
    L.append(d)
print(L)
# 2)解法

# 方法1
# print('+-------------+-------+---------+')
# print('|    name     |  age  |  score  |') 
# print('+-------------+-------+---------+')
# for d in L:
#     k11 = (13 - len(d['name'])) // 2
#     k12 = 13 - k11 - len(d['name'])

#     s1 = str(d['age'])
#     s2 = str(d['score'])
#     k31 = (9 - len(s2)) // 2
#     k32 = 9 - k31 - len(s2) 

#     print('|' + ' ' * k11 + d['name'] + ' ' * k12 +
#         '|' + ' ' * 2 + s1 + ' ' * 3 +
#         '|' + ' ' * k31 + s2 + ' ' * k32 + '|')
# print('+-------------+-------+---------+')

# 方法2
print('+-------------+-------+---------+')
print('|    name     |  age  |  score  |') 
print('+-------------+-------+---------+')
for d in L:
    t = (d['name'].center(13), str(d['age']).center(7), str(d['score']).center(9))
    line = "|%s|%s|%s|" % t  # t是元组
    print(line)
print('+-------------+-------+---------+')
