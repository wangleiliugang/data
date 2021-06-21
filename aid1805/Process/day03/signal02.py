from signal import *
import os, time


# 信号处理函数，有固定参数格式
def handler(sig, frame):
    if sig == SIGALRM:
        print("收到了时钟信号")
    elif sig == SIGINT:
        print("收到了SIGINT信号，结束！")


alarm(5)


# 通过函数处理信号
signal(SIGALRM, handler)
signal(SIGINT, handler)

# pause()

while True:
    print('wait for signal...')
    time.sleep(2)
