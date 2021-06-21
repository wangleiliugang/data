# 此示例示意time_sleep 用法
import time
print("开始打印...")
time.sleep(1)
print("程序结束")


import time
print("开始打印...")
time.sleep(1)
print("还剩2秒")
time.sleep(1)
print("还剩1秒")
print("程序结束")

# 写一个程序，输入你的出生日期
#　1.算出你已经出生了多少天？
#　2.算出你出生那天是星期几？
import time

year = int(input("请输入出生年份："))
month = int(input("请输入出生月份："))
days = int(input("请输入出生日："))
birthday_secs = time.mktime((year,month,days,0,0,0,0,0,0))    # 得到出生时的秒数
cur_secs = time.time()                                        # 得到当前时间的秒数
s = cur_secs - birthday_secs                                  # 算出您已经出生了多少天
print("您已经出生了：", s / 60 / 60 // 24, "天")

birthday = (year,month,days,0,0,0,0,0,0)    # 得到出生时的时间元组
s = time.mktime(birthday)                   # 转为秒数
t = time.localtime(s)                       # 转回到时间本地元组
weekday = {0:'星期一', 1:'星期二', 2:'星期三', 3:'星期四', 4:'星期五', 5:'星期六', 6:'星期日'}
print("您出生那天是：", weekday[t[6]])

