# 此示例示意return 语句的用法和执行过程

def myf1():
    print('aaaaaaaaa')
    print('bbbbbbbbb')
    return             # return 100
    print("ccccccccc")
v = myf1()
print('v =', v)

# 写一个函数　mymax, 实现返回两个数的最大值：

# 方法1
def mymax(a, b):
    if a >= b:
        s = a
    else:
        s = b
    return s
# 方法2
#def mymax(a, b):
#    if a >= b:
#        return a
#    else:
#        return b
# 方法3
#def mymax(a, b):
#    if a >= b:
#        return a
#    return b    

print(mymax(100, 200))
print(mymax(50, 10))
print(mymax('ABC', 'ABCD'))


# 写一个函数　input_number
# def input_number():
#     ....
# 此函数用来获取用户循环输入的整数，当用户输入负数时结束输入，将用户输入数以列表的形式返回，再用内建函数max, min, sum打印结果．

def input_number():
    L = []
    while True:
        i = int(input('请输入整数：'))
        if i >= 0:                       # if i < 0:
            L.append(i)                  #     return L
        else:                            # L.append(i)
            break
    return L
def main():
    L = input_number()
    print(L)
    print("用户输入的最大数是：", max(L))
    print("用户输入的最小数是：", min(L))
    print("用户输入数的和是：", sum(L))
main()


















