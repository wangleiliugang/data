# -*- coding: utf-8 -*-


def Fab(n):
    """
    使用非递归来实现一个斐波那契数列Fab(n),并使用yield来返回值
    """
    a, b, m = 0, 1, 0
    while m < n:
        yield b
        a, b, m = b, a + b, m + 1


t = Fab(20)
print("变量t的类型为: ", type(t))
# for i in t:
#    print(i)

print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
