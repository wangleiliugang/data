# 示例1
def f1():
    print("f1被调用")
fx = f1
fx()   # 等同于　f1()

# 示例2
def f1():
    print("hello")
def f2():
    print("world")
f1, f2 = f2, f1   # 交换两个变量的绑定关系
f1()

# 此示例示意一个函数作为另一个函数的参数传递
def f1():
    print("hello,")
def f2():
    print("world!")
def fx(fn):
    print(fn)
    fn()
fx(f1)
fx(f2)

# 看懂下面的函数在做什么
def fx(a, fn):
    return fn(a)

L = [5, 9, 4, 6]
print("最大值是：", fx(L, max))
print("最小值是：", fx(L, min))
print("和是：", fx(L, sum))

# 此示例示意函数作为函数的返回值
def get_fx():
    s = input('请输入您要执行的操作(求最大/求最小/求和)：')
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 6, 8, 10]
print(L)
f1 = get_fx()
print(f1(L))

# 写一个计算器的解释执行器
# 已知有如下函数：
#　def myadd(x, y):     # 计算两个数相加
#　　　　　return x + y
# def mymul(x, y):     # 计算两个数相乘
#　　　　　return x * y
#
# def get_op(s):       # s代表操作字符串：'加'，'乘'
#     此处自己实现 
# 主函数：
# def main():
#     while True:
#         s = input('请输入计算公式：')　　　　# 如10　加　20
#         L = s.split()
#         a, s, b = L
#         a, b = int(a), int(b)
#         fn = get_op(s)
#         print("结果是：", fn(a, b))     # 结果是30


def myadd(x, y):     # 计算两个数相加
    return x + y
def mymul(x, y):     # 计算两个数相乘
    return x * y
def get_op(s):
    if s == '加' or s == '+':
        return myadd
    elif s == '乘' or s == '*':
        return mymul

def main():
    while True:
        s = input('请输入计算公式：')
        L = s.split()
        a, s, b = L
        a, b = int(a), int(b)
        fn = get_op(s)
        print("结果是：", fn(a, b)) 
main()

# 此示例示意函数的嵌套
def fn_outer():
    print("fn_outer被调用！")
    def fn_inner():
        print("fn_inner被调用！")
    fn_inner()
    fn_inner()
    print("fn_outer调用结束！")
    return fn_inner

fn_outer()
print('-------------------------')
fx = fn_outer()
fx()      # 调用fn_outer内部创建的函数

















