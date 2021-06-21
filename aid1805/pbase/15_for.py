# 此示例示意for　语句循环遍历　可迭代对象中的数据

s = 'EDCBA'
for ch in s:
    print('ch--', ch)
else:
    print("for 语句执行else 子句")
print("程序退出！")

# 任意输入一个字符串，判断这个字符串中有几个空格' '(要求不允许使用s.count方法)，建议时使用for 语句实现
count = 0
n = input("请输入一个字符串：")
for ch in n:
    if ch == ' ':
        count += 1
print("字符串中空格有：",count ,'个')


# 此示例示意range 函数的用法

for x in range(4):
    print(x)


for x in range(3, 6):
    print(x)


# 用for 语句打印1～20的整数，打印在一行　　1，2，3，．．．，19，20

for x in range(1, 21):
    print(x, end=' ')
print()


# 求100　以内有哪些整数与自身加1　的乘积再对11　求余结果等于８

for x in range(100):
    i = (x *(x + 1)) % 11
    if i ==8:
        print(x)


# 计算1+　3+　5+　7+　．．．+　99的和，用while 和for 语句两种方法实现

s = 0 #此变量用来保存求和结果
i = 1 #
while i < 100:
    s += i
    i += 2
print('和为：', s)


a = 0
for x in range(1, 100, 2):
    a += x
print('和为：', a)


for x in "ABC":
    for y in '123':
        print(x + y)























