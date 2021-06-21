# 此示例示意函数的缺省参数

def info(name, age=1, address='未填写'):
    print(name, "今年", age, '岁，家庭地址是：', address)
info('tarena', 15)
info('小王', 20, '江苏苏州')
info('小明')


# 写一个函数mysum(), 可以传入两个实参或例者三个实参
# 1.如果传入两个实参，则返回两个实参的和
# 2.如果传入三个实参，则返回前两个实参的和对第三个实参求余的结果
# 如：print(mysum(1, 100))       # 101
#    print(mysum(2, 10, 7))     # 5

def mysum(x, y, z=None):
    if not z:             # if z is None:
        return (x + y)
    return (x + y) % z

print(mysum(1, 100))
print(mysum(2, 10, 7))

# 此示例示意星号元组形参
def func(*args):
    print('参数个数是：', len(args))
    print('args =', args)

func(1, 2, 3, 4)
func('hello', 'world', 1, 2, 3)

# 写一个函数mysum, 可以传入任意个实参的数字，返回所有实参的和
# def mysum(...):
#     ...
# print(mysum(1, 2, 3, 4))    # 10
# print(mysum(2, 4, 6))       # 12

# 方法1
def mysum(*args):
    return sum(args)
print(mysum(1, 2, 3, 4, 5))
print(mysum(2, 4, 6))
# 方法2
def mysum1(*args):
    i = 0
    s = 0
    len(args)
    while True:
        if i < len(args):
            s += args[i]
            i += 1
        else:
            break
    return s
print(mysum1(1, 2, 3, 4, 5))
print(mysum1(2, 4, 6))
# 方法3
def mysum2(*args):
    s = 0
    for x in args:
        s += x
    return s
print(mysum2(1, 2, 3, 4, 5))
print(mysum2(2, 4, 6))

# 此示例示意命名关键字形参

def fn(*, d, e):
    print("d=", d)
    print("e=", e)
fn(d=100, e=200)     # 合法调用
# fn(1, 2)             不合法，不能用位置传参

def fm(*args, d, e):
    print(args)
    print('d=', d)
    print('e=', e)
fm(1, 2, d=100, e=200)
fm(*'AB', **{'e':20, 'd':10})

# 此示例示意双星号字典形参

def func(**kwargs):
    print('关键字参数个数是：', len(kwargs))
    print("kwargs=", kwargs)
func(name='tarena', age=15)
func()

# 综合示例

def f1(a, b, *args, c, **kwargs):
    print(args)
    print(kwargs)
f1(1, 2, 3, 4, d=6, c=5, e=7)
f1(*"hello", d=6, **{'c':5, 'e':7})

# 写一个myrange 函数，此函数返回一个符合range规则的整数列表
# 如：L = myrange(3)         print(L)     # [0,1,2]
#    L = myrange(3, 6)      print(L)     # [3,4,5]
#    L = myrange(1, 10, 3)  print(L)     # [1,4,7]

# 方法1
def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    L = []
    i = start
    while i < stop:
        L.append(i)
        i += step
    return L

print(myrange(5))
print(myrange(3, 6))
print(myrange(1, 10, 3))
print(myrange(5, 0, -2))      # 此处出错，方法2优化

# 方法2
def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    L = []
    i = start
    if i < stop:
        while i < stop:
            L.append(i)
            i += step
    else:
        while i > stop:
            L.append(i)
            i += step
    return L

print(myrange(5))
print(myrange(3, 6))
print(myrange(1, 10, 3))
print(myrange(5, 0, -2))
