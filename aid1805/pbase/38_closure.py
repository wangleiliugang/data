# 此示例示意闭包的创建和调用过程
def make_power(y):
    def fx(arg):
        return arg ** y
    return fx
pow2 = make_power(2)
print('3的平方是：', pow2(3))
pow3 = make_power(3)
print('3的立方是：', pow3(3))
# 求1 ** 2 + 2 ** 2 + 3 ** 2 + ... + 9 ** 2 的和
print(sum(map(lambda x: x ** 2, range(1, 10))))
print(sum(map(make_power(2), range(1, 10))))

# 用参数返回相应的数学函数的示例
# y = a * x ** 2 + b * x + c
def make_function(a, b, c):
    def fx(x):
        return a * x ** 2 + b * x + c
    return fx
# 创建一个y = 4 * x ** 2 + 5 * x + 6　的函数用fx1绑定
fx1 = make_function(4, 5, 6)
print(fx1(2))   # 求在x等于2时，y的值

