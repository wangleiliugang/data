# 此示例示意位置传参/序列传参/关键字传参/字典关键字传参

def myfun(a, b, c):
    print("a绑定的是：", a)
    print("b绑定的是：", b)
    print("c绑定的是：", c)

myfun(1, 2, 3)

s = [1, 2, 3]
myfun(*s)
s2 = "ABC"
myfun(*s2)

myfun(b=22, c=33, a=11)
myfun(c=3, b=2, a=1)

d = {'c':33, 'b':22, 'a':11}
myfun(**d)

# 写一个函数sum3(a, b, c):    用于返回三个数的和
# 写一个函数pow3(x):          用于返回x　的三次方(立方)
# 1．用以上函数计算，　1**3 + 2**3 + 3**3 
# 2.计算，　1　+　2　+　3　的和的立方，即(1+2+3)**3

def sum3(a, b, c):
    s = a + b + c
    return s
def pow3(x):
    p = x ** 3
    return p
print('三个数立方的和是：',sum3(pow3(1), pow3(2), pow3(3)))
print('三个数和的立方是：',pow3(sum3(1, 2, 3)))




























