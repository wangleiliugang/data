# while.py

# 此示例示意while 语句的用法

i = 1
while i <= 20:
    print("hello world!")
    i += 1
else:
    print("条件不满足，循环程序结束！")
print("上一条while 语句结束，此时变量i=", i)

n = int(input("请输入需要打印的行数："))
while 1 <= n:
    print("hello world!")
    n -= 1
print("程序结束！")


# 用while 语句打印1~20 的整数(包含20)

i = 1
while i <= 20:
    print(i)
    i += 1
print("程序结束！")


# 输入一个整数，用end 变量绑定，打印出1~end 的所有整数(包括end)

end = int(input("请输入一个整数："))
i = 1
while i <= end:
    print(i)
    i += 1
print("程序结束！")


# 写程序，输入两个整数，第一个用begin 绑定，第二个用end 绑定，打印出begin~end的所有整数

begin = int(input("请输入第一个整数："))
end = int(input("请输入第二个整数："))
while begin < end:
    print(begin)
    begin += 1
else:    
    while begin >= end:
        print(end)
        end += 1
print("程序结束！")


# 打印1～20的整数，打印在一行内显示，每个数字之间用一个空格分隔开

i = 1
while i <= 20:
    print(i, end=' ')
    i += 1
else:
    print()


# 打印1～20的整数，每行5个，打印四行，每个数字之间用一个空格分隔开

i = 1
while i <= 20:
    print(i,end=' ')
    if i % 5 ==0:
        print()
    i += 1


# 用while 语句打印10～1的所有整数(包含1)

i = 10
while i >= 1:
    print(i)
    i -= 1
print("程序结束！")


# 写程序，用　while 循环计算　1+　2+　3+　4+　．．．．．．+　99+　100的和

s = 0       #　此变量保存所有数的和
i = 1
while i <=100:
    s += i  # 把当前的数累加到一个变量中
    i += 1
print("1+　2+　3+　4+　．．．．．．+　99+　100的和:",s)


# 用while 语句实现打印三角形，输入一个整数，表示三角形的宽度和高度，打印出相应的直角三角形
# 例如:请输入三角形宽度：4　　　　　则打印如下：
#                          *
#                          **
#                          ***
#                          ****

w = int(input('请输入三角形宽度：'))
i = 1
while i <= w:
    print('*' * i)
    i += 1


# 打印1～20的整数，打印在一行内显示，每个数字之间用一个空格分隔开（重复打印10行）

j = 1
while j <= 10:
    i = 1
    while i <= 20:
        print(i, end=' ')
        i += 1
    else:
        print()
    j += 1


# 输入一个数，打印指定宽度的正方形
# 如输入：5　　则打印如下：
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5

n = int(input("请输入正方形的宽度："))
j = 1
while j <= n:

    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1
    print()
    j += 1











