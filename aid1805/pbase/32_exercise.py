# 1.写一个函数mysum(n)，要求给出一个数n, 求1 + 2 + 3 + 4 + ... + n 的和
# 如：print(mysum(100))      # 5050
#    print(mysum(10))      # 55
# 方法1
def mysum(n):
    return sum(range(1, n + 1))


print(mysum(100))
print(mysum(10))

# 方法2
mysum1 = lambda n: sum(range(0, n + 1))
print(mysum1(100))
print(mysum1(11))

# 2.写一个函数myfac(n)来计算n!(n的阶乘)
# n! = 1*2*3*4*...*n
# 如：print(myfac(5))      # 120
#    print(myfac(4))      # 24


def myfac(n):
    s = 1
    for x in range(1, n + 1):
        s *= x
    return s


print(myfac(5))
print(myfac(4))

# 3.写一个函数，求　1　+　2**2　+　3**3　+　... + n**n　的和
# 方法1


def myfn(n):
    s = 0
    for x in range(1, n + 1):
        s += x**x
    return s


print(myfn(2))
print(myfn(3))

# 方法2


def myfn(n):
    return sum(map(lambda x: x**x, range(1, n + 1)))


print(myfn(2))
print(myfn(3))
