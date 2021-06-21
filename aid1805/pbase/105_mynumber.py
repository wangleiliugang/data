# 此示例示意运算符重载

class MyNumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    # def myadd(self, other):
    #     v = self.data + other.data
    #     return MyNumber(v)

    def __add__(self, other):
        print("__add__被调用！")
        v = self.data + other.data
        return MyNumber(v)

    def __sub__(self, other):
        v = self.data - other.data
        return MyNumber(v)

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.myadd(n2)

# n3 = n1.__add__(n2)
n3 = n1 + n2
print(n3)
n4 = n3 - n2
print(n4)


# # 练习：实现两个自定义列表相加
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, rhs):
        iterable = self.data + rhs.data
        return MyList(iterable)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 2
print(L5)  # MyList([1, 2, 3, 1, 2, 3])

# # 以下错误的解决办法必须用反向运算符的重载
# L6 = 2 * L1  # 会出错
# print(L6)


# 此示例示意反向运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __mul__(self, rhs):
        print("__mul__被调用！")
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        print("__mul__被调用！")
        return MyList(self.data * lhs)

L1 = MyList([1, 2, 3])
L5 = L1 * 2
print(L5)

L6 = 2 * L1
print(L6)


# 此示例示意复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, rhs):
        print("__add__被调用!")
        return MyList(self.data + rhs.data)

    def __iadd__(self, rhs):
        print("__iadd__被调用!")
        self.data.extend(rhs.data)
        return self

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L1 += L2  # 当没有__iadd__方法时，等同于调用L1 = L1 + L2
print(L1)


# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __neg__(self):
        # L = [-x for x in self.data]
        L = (-x for x in self.data)
        return MyList(L)

L1 = MyList([1, -2, 3, -4])
L2 = -L1
print(L2)


# 此示例示意in / not in 运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __contains__(self, e):
        for x in self.data:
            if x == e:
                return True        
        return False

L1 = MyList([1, -2, 3, -4])
if -2 in L1:
    print("-2 在L1中")
else:
    print("-2 不在L1中!")
# 当MyList类内重载了__contains__方法时，in 和 not in 可以同时使用
if -3 not in L1:
    print("-3 不在L1中")
else:
    print("-3 在L1中")


# 此示例示意索引和切片运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __getitem__(self, i):
        print("__getitem__被调用，i=", i)
        # if type(i) is not int:
            # raise TypeError
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用，i=", i, "v=", v)
        self.data[i] = v  # 修改data绑定的列表


L1 = MyList([1, -2, 3, -4])
v = L1[0]
print(v)
# print(L1["hello"])

L1[1] = 2
print(L1)