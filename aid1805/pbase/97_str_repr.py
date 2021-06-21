# 示例1
class MyNumber:
    def __len__(self):
        return 100

n1 = MyNumber()
x = len(n1)  # 重写了__len__方法才可以
print('x =', x)


# 此示例示意一个自定义的数字类型重写repr和str 的方法
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        return "数字: %d" % self.data

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

n1 = MyNumber(100)
print(str(n1))  # 相当于调用 n1.__str__(self)
print(repr(n1))
print(n1)  # 调用__str__方法 >>># 数字:100

n2 = eval("MyNumber(100)")


# 此示例示意自定义的类MyNumber能够转成为数值类型
class MyNumber:
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        return 'MyNumber(%d)' % self.data
    def __int__(self):
        '''此方法用于int(obj)函数重载，必须返回整数
        此方法通常用于制定自定义对象如何转为整数的规则'''
        return 10000

n1 = MyNumber(100)
print(type(n1))
# if n1 == 100:
    # print("n1 == 100")
n = int(n1)
print(type(n))

