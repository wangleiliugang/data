# 一个公司有两种职位：经理，技术员
# 其中经理：曹操，　刘备，　孙权
#  技术员：曹操，　孙权，　张飞，赵云
# 用集合求：1.既是经理也是技术员的有哪些人？
#        2.是经理，但不是技术员的有谁？
#        3.是技术员，不是经理的都有谁？
#        4.张飞是经理吗？
#        5.身兼一职的人有谁？
#        6.经理和技术员一共有几个人？

s1 = {'曹操', '刘备', '孙权'}
s2 = {'曹操', '孙权', '张飞', '赵云'}
s11 = s1 & s2
print(s11)
s22 = s1 - s2
print(s22)
s33 = s2 - s1
print(s33)
if '张飞' in s1:
    print('张飞是经理')
else:
    print('张飞不是经理')
print(s1 ^ s2)
print('共有%d 人' % len(s1 | s2))


# 任意输入一个单词，存入集合中，当输入空字符串时结束输入
# 1)打印您输入的单词的种类数(去重)
# 2)每个单词都打印到终端上显示

s = set()
while True:
    n = input('请输入单词：')
    if n == '':               # if not s:  也可以
        break
    s.add(n)
print('您共输入%d 种单词'% len(s))
print(s)

# 思考：如何让打印的次序和输入的次序一致？

L = []
L2 = []
while True:
    n = input('请输入单词：')
    if n == '':              # if not s:  也可以
        break
    L.append(n)
print(L)
# 方法1                    # 方法2
for x in L:               #s = set(L)
    if x not in L2:       #for x in L:
        L2.append(x)      #    if x in s:
print(L2)                 #        print(x)     
for x in L2:              #        s.discard(x)
    print(x)

# 模拟一个点名系统，已知全班学生名单，随机打印学生的姓名进行点名，并得到此学生是否已到信息，输入'y'代表已到，输入'n'代表未到场
# 点名结束后打印未到场学生名单

s = {'小张', '小王', '小李', '小明', '小红', '小花', '小虎', '小赵'}

s1 = set()
for x in s:
    print(x)
    i = input('未到请输入n,其它输入代表到场:')
    if i == 'n': 
        s1.add(x)
if s1 != set():
    print('未到学生名单如下：')
    for x in s1:
        print(x)
if s1 == set():
    print('全部到场')




























