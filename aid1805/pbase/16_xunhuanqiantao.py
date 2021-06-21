# 写程序，输入一个整数n　,代表正方形的宽度和高度，打印　数字组成的正方形
# 如输入数字：４
#           1　2　3　4　
#           1　2　3　4　
#           1　2　3　4　
#           1　2　3　4　

n = int(input("请输入一个整数："))
for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(y, end=' ')
    print()


# 如输入数字：４
#           1　2　3　4　
#           2　3　4　5
#           3　4　5 6
#          　4　5 6 7

i = 1
n = int(input("请输入一个整数："))
for x in range(1, n + 1):
    for y in range(i, n + i):
        print(y, end=' ')
    i += 1
    print()

w = int(input("请输入一个整数："))
for y in range(1, w + 1):
    for x in range(y, y + w):
        print("%2d" % x, end=' ')
    print()

# 示意continue 语句在for 语句中的用法

for x in range(5):
    if x == 2:
        continue
    print(x)


# 输入一个整数用begin绑定，再输入一个整数用end绑定，打印出从begin~end(包含end)的所有偶数
# (建议用continue语句跳过奇数)

begin = int(input("请输入第一个整数："))
end = int(input("请输入第二个整数："))
if begin <= end:
    for x in range(begin, end + 1):
        if x % 2 == 1:
            continue
        print(x)

if end <= begin:
    for x in range(end, begin + 1):
        if x % 2 == 1:
            continue
        print(x)


# 用continue 和while 语句，实现打印10以内的偶数

i = 0
while i < 10:
    if i % 2 == 1:
        i += 1      # 在continue语句进入死循环之前改变变量的值
        continue
    print(i)
    i += 1


# 求1～100(包含100)之间所有不能被5，7，11整除的数的和是多少？(建议用continue 语句实现)

s = 0
i = 1
while i <= 100:
    if i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
        i += 1
        continue
    s += i
    i += 1
print(s)


s = 0
for x in range(1, 101):
    if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        continue
    s += x
print(s)




