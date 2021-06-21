# 此示例示意生成器函数的定义及使用

def myyield():
    yield 2
    yield 3
    yield 5
    yield 7

for x in myyield():
    print(x)

# gen = myyield()  # gen绑定生成器
# it = iter(gen)   # it绑定迭代器
# print(next(it))

# 1.写一个生成器函数
# def myinteger(n):
#     ...
# 此生成器函数可以生成从0开始，到n结束(不包含n)的一系列整数
# for x in myinteger(3):
#     print(x)  # 0, 1, 2
# 方法１
# def myinteger(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1

# 方法２
def myinteger(n):
    for i in range(n):
        yield i

for x in myinteger(3):
    print(x) 

# it = iter(myinteger(2))
# print(next(it))
# print(next(it))
# print(next(it))


# 2.写一个生成器函数myodd(x)，生成一系列奇数
def myodd(x):
    for i in range(x + 1):
        if i % 2 == 1:
            yield i

for x in myodd(10):
    print(x)