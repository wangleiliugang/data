# 此示意break 语句的用法

i = 1
while i <=6:
    print("本次循环开始时：",i )
    if i ==3:
        break
    print("本次循环结束时：",i)
    i += 1
print("这是程序最后一条语句！i=",i )


# 任意输入一些整数，当输入负数时结束输入，当输入完成后，打印您输入的这些数的和

s = 0
while True:
    n = int(input("请输入一个整数："))
    if n < 0:
        break
    s += n
print(s)


# 写程序用while 语句实现打印三角形
#　要求输入一个整数表示三角形的宽度和高度，打印出如下的三角形
# 1.   *       2.****      3.****
#     **          ***        ***
#    ***           **        **
#   ****            *        *

n = int(input("请输入三角形的宽度："))

i = 1                               # i = 1
while True:                         # while i <= n:
    print(' ' * (n - i) + '*' * i)  #     print(' ' * (n - i) + '*' * i)
    if i >= n:                      #     i += 1
        break                       # 
    i += 1                           
                           

print("－－－第二个三角形－－－")    
a = 0
while True:
    print(' ' * a + '*' * (n - a))
    if a >= n:
        break
    a += 1


print("－－－第三个三角形－－－") 
b = 0
while True:
    print('*' * (n - b) + ' ' * b)
    if b >= n:
        break
    b += 1
print()


# 写程序求多项式的和　：1/1 - 1/3 + 1/5 - 1/7 + 1/9... + 1/(2*n - 1) 的和　，n最大取：1000000
# 1.打印这个多项式的和　　　　　2.打印这个多项式和乘以4

s = 0                           # 方法2
n = int(input("请输入n 的值："))  # s = 0
i = 1                           # sign = 1
while i <= n:                   # i = 1
    x = 1 / (2 * i - 1)         # while i <= 1000000:
    if i % 2 == 1:              #     s += sign * 1 / (2 * n - 1)
        s += x                  #     sign *= -1
    else:                       #     i += 1
        s += -x                 # prrint(s, s * 4)
    i += 1
print(s)
print(s * 4)





















