#! /usr/bin/python3

print("hello world!")
print("hello tarena!")
print("today is friday!")


print(1 + 2)


print("*******")
print("*     *")
print("*     *")
print("*******")

print("这个矩形的周长是：", (6 + 4) * 2)
print("这个矩形的面积是：", 6 * 4)

r = 3
pi = 3.1415926
length = 2 * pi * r
area = pi * r ** 2
print("这个圆的周长是：", length)
print("这个圆的面积是：", area)

a = 10
b = 20
# 以下实现交换算法（经典交换算法）
temp = a
a = b
b = temp
print(a, b)

a = 10
b = 20
# 序列赋值
a, b = b, a
print(a, b)

print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")

print("216两是：", 216 // 16, "斤", 216 % 16, "两")
print("现在时间是：", 63320 // 3600, ":", 63320 % 3600 // 60, ":", 63320 % 3600 % 60)


s = input("请输入字符串：")
print("您输入的字符串是：", s)

i = int(s)
print(i + 1)


print(1, 2, 3, 4)
print(1, 2, 3, 4, sep="#")
print(1, 2, 3, 4, end="\n\n\n\n\n")    # 换５行
print(6789, end="")    # 不换行
print("我是程序最后一行")

age = 20
days = 365 * 20
weeks = days // 7
day = days % 7
print("小明过了：", weeks, "星期", day, "天")


a = input("请输入当前小时数：")
hour = int(a)
b = input("请输入当前分钟数：")
minute = int(b)
c = input("请输入当前秒数：")
second = int(c)
seconds = hour * 60 * 60 + minute * 60 + second
print("距离凌晨0:0:0过了：", seconds, "秒")
