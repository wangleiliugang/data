#　1.编写函数求阶乘myfac(x),什么方法都可以
def myfac(x):
    if x ==1:
        return 1
    return x * myfac(x - 1)

# 2.写程序算出1-20　的阶乘的和：1！+2！+3！+．．．+20！
# 方法1
print(sum(map(myfac, range(1, 21))))

# 方法2
s = 0
for x in map(myfac, range(1, 21)):
    s += x
print(s)

# 3.已知有列表：L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#  (1)写一个函数print_list(lst) 打印出所有元素print_list(L) # 打印...
#  (2)写一个函数sum_list(lst)  返回这个列表中所有元素的和
#  注：type(x)可以返回一个变量的类型
#  如: type(20) is int            # True
#     type([1, 2, 3]) is list     # True
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def print_list(lst):
    for x in lst:
        if type(x) is int:
            print(x)
        else:
            print_list(x)
print_list(L)

def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is list:
            s += sum_list(x)
        else:
            s += x
    return s
print(sum_list(L))

