# 此示例示意函数递归
def fa():
    fb()
def fb():
    fa()
#fa()
print("递归结束")

# 控制递归层次的示例：
def fx(n):
    print("递归进入第", n, "层")
    if n == 3:
        return
    fx(n + 1)
    print("递归退出第", n, "层")

fx(1)
print("程序结束")

# 求和1 + 2 + 3 + 4 + ...+ 100的和
def mysum(x):
    if x < 1:        # if x <= 1:
        return 0     #     return 1
    return x + mysum(x - 1)

s = mysum(100)
print(s)

# 练习：编写程序用递归求阶乘：
#      def myfac(x):
#          ...
#      print(myfac(5))    120
#      print(myfac(4))    24
def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x - 1)

print(myfac(5))
print(myfac(4))

