# 练习：
# 售票员和司机的故事
# 1.创建父子进程，分别表示司机和销售员
# 2.当售票员捕捉到SIGINT信号时，给司机发送SIGUSR1信号，司机打印"老司机开车了"
#   当售票员捕捉到SIGQUIT信号时，给司机发送SIGUSR2信号，司机打印"系好安全带，小心甩出去"
#   当司机捕捉到SIGTSTP信号时，给售票员发送SIGUSR1信号，售票员打印"到站了，下车吧"
# 3.到站后，售票员先下车(子进程先退出)，然后司机下车

from multiprocessing import Process
from signal import *
import os
import time


def saler_handler(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)  # 给父进程发送信号
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了，下车吧")
        os._exit(0)


def driver_handler(sig, frame):
    if sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("系好安全带，小心甩出去")
    elif sig == SIGTSTP:
        os.kill(p.pid, SIGUSR1)  # 给子进程发送信号


def saler():
    signal(SIGINT, saler_handler)
    signal(SIGQUIT, saler_handler)
    signal(SIGUSR1, saler_handler)
    signal(SIGTSTP, SIG_IGN)
    while True:
        time.sleep(2)
        print("继续行使中...")


# 设置driver为父进程，saler为子进程
p = Process(target=saler, name='spy')
p.start()

# 父进程处理信号部分
signal(SIGUSR1, driver_handler)
signal(SIGUSR2, driver_handler)
signal(SIGTSTP, driver_handler)
signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)

p.join()
