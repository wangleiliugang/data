# 猜数字游戏：
# 写程序，随机生成一个0~100之间的数用变量x绑定，循环让用户输入一个数用y绑定，输出猜数字的结果
# 1.如果y等于生成的数x，则提示'您猜对了'，打印出猜测的次数并退出
# 2.如果y小于x则提示'您猜小了'，然后继续猜
# 3.如果y大于x则提示'您猜大了'，然后继续猜
# 猜对后程序退出并打印次数

def mygames():
    import random as r
    x = r.randrange(101)
    print("系统随机生成的数是：",x)
    times = 0
    while True:
        y = int(input("请输入猜测的数字："))
        times += 1
        if y == x:
            print("您猜对了")
            break
        elif y < x:
            print("您猜小了")
        elif y > x:
            print("您猜大了")
    return times

print("您猜对这个数共用了：%d 次" % mygames())

# 原理：二分查找　　　　　　(前提序列有序)
# import math ----> math.log(101, 2)
