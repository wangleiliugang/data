# 1.写一个程序，以电子时钟格式打印时间：
# 时间格式为：HH:MM:SS
# 时间每隔一秒刷新一次
# 方法1
# import time
# while True:
#    now_secs = time.time()
#    now_time = time.localtime(now_secs)
#    print(now_time[3],':',now_time[4],':',now_time[5],)
#    time.sleep(1)

# 方法2
import time


def clock():
    while True:
        cur_time = time.localtime()
        t_hms = cur_time[3:6]
        print("%02d:%02d:%02d" % t_hms, end='\r')
        time.sleep(1)
# clock()

# 2.编写一个闹钟程序，启动时设置定时时间，到时候打印出一句语句，然后程序退出
# 方法1
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# days = int(input("请输入日期："))
# hours = int(input("请输入小时："))
# minutes = int(input("请输入分钟："))
# seconds = int(input("请输入秒数："))
# timing = time.mktime((year,month,days,hours,minutes,seconds,0,0,0))
# cur_secs = time.time()
# s = timing - cur_secs
# time.sleep(s)
# print("现在时间按是：", year,'年',month,'月',days,'日',hours,'时',minutes,'分',seconds,'秒')

# 方法2


def alarm(hour, minute):
    while True:
        cur_time = time.localtime()
        tuple_hm = cur_time[3:5]
        print("%02d:%02d:%02d" % cur_time[3:6], end='\r')
        if (hour, minute) == tuple_hm:
            break


def main():
    h = int(input("请输入小时："))
    m = int(input("请输入分钟："))
    alarm(h, m)
    print("\n时间已到！")


main()

# 3.请编写函数fun,其功能是计算下列多项式的和
# sn = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
# 计算n为100时的值，看一下求出来的和是什么？(建议用math.factorial)
# 方法1
import math


n = int(input("请输入n的取值："))
s = sum(map(lambda n: 1 / math.factorial(n), range(n + 1)))
print(s)


# 方法2
def fun(n):
    n = int(input("请输入n的取值："))
    formula = lambda x: 1 / math.factorial(x)
    return sum(map(formula, range(n + 1)))


print(fun(100))
