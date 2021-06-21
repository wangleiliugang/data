# 写一个lambda　表达式，判断这个数的2次方+1是否能被5整除，如果能整除返回True,否则返回False
# fx = lambda n: ...
# print(fx(3))    # True
# print(fx(4))    # True
# 方法1
fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False
print(fx(3))
print(fx(4))
# 方法2
fx = lambda n: (n ** 2 + 1) % 5 == 0
print(fx(3))
print(fx(4))

# 写一个lambda 表达式，求两个变量的最大值：
# def mymax(x, y):
#     ...
# 或用 lambda
# mymax = lambda ...
# print(mymax(100, 200))     # 200


# 方法1
def mymax(x, y):
    return(max(x, y))
print(mymax(100, 200))
# 方法2
mymax = lambda x, y:max(x, y)
print(mymax(100, 200))
# 方法3
mymax = lambda x, y:x if x > y else y
print(mymax(200, 100))


# 看懂下面的程序在做什么？
def fx(f, x, y):
    print(f(x, y))
fx((lambda a, b: a + b), 100, 200)
fx((lambda a, b: a ** b), 3, 4)
