# 此示例示意用def　语句来创建函数及自定义函数的调用

def say_hello():
    print("hello world!")
    print("hello tarena!")
    print("hello everyone!")
# 调用say_hello() 函数
say_hello()


def mymax(a, b):
    print('a = ', a)
    print('b = ', b)
    if a > b:
        print(a, '大于', b)
    else:
        print(a, '小于等于', b)
mymax(1, 2)
mymax(100, 50)
mymax('abc', '123')

# 1.写一个函数myfun, 此函数用显示两个参数的相关信息
# 函数：def myfun(a, b):
# 此函数给定两个参数，打印关于两个参数的信息：
# 1)打印两个参数的最大值
# 2)打印两个参数的和
# 3)打印两个参数的积
# 4)打印从a　开始到b 结束的所有偶数

def myfun(a, b):
    print('a = ', a)
    print('b = ', b)
    if a >= b:
        print('最大值是：', a)
    else:
        print('最大值是：', b)
    s = a + b
    print('和是：', s)
    i = a * b
    print('积是：', i)
    print(a,'到',b,"之间的偶数有：", end='')
    for n in range(a, b):
        if n % 2 == 0:
            print(n ,end=' ')
    print()
myfun(3, 10)
myfun(10, 20)
myfun(15, 15)
myfun(-12, -3)


# 2.猴子吃桃
# 有一只小猴子，摘了很多桃．第1天吃了全部桃子的一半，感觉不饱又吃了一个;第2天吃了剩下的一半，感觉不饱又吃了一个;...以此类推
#　到第10天，发现只剩下一个了
#　请问第一天摘了多少桃？

def get_yesterday(y):
    x = (y + 1) * 2
    return x
p = 1
day = 10
while day > 1:  
    day -= 1
    p = get_yesterday(p)
    print('第', day, '天的桃子数是：', p)


# 3.完全数：
# 1 + 2 + 3 = 6 (6为完全数)
# 1, 2, 3 都为6　的因数(能被一个数x 整除的数为y ,则y　为x 的因数)
# 1 * 6 = 6
# 2 * 3 = 6
# 完全数是指除自身以外，所有的因数相加之和等于自身的数
# 求4~5个完全数并打印出来

# 方法1
def is_perfect_number(i):
    L = []
    for x in range(1, i):
        if i % x == 0:
            L.append(x)
    if sum(L) == i:
        return True
    return False

def main():
    i = 1
    while True:
        if is_perfect_number(i):
            print(i, "是完全数")
        i += 1
main()


# 方法2
i = 1                          # 完全数的开始值
while True:
    L = []
    for x in range(1, i):
        if i % x == 0:
            L.append(x)
    if sum(L) == i:
        print(i, '是完全数')
    i += 1













