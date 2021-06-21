import signal
import time

signal.alarm(5)
# 采用默认方式处理
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGALRM, signal.SIG_DFL)

# 忽略该信号
# signal.signal(signal.SIGINT,signal.SIG_IGN)
# signal.signal(signal.SIGALRM,signal.SIG_IGN)

while True:
    time.sleep(2)
    print("按ctrl + c触发信号")
