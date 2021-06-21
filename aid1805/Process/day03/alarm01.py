import signal
import time


# 3秒后向自己发送一个SIGALRM时钟信号
signal.alarm(3)
signal.alarm(8)

# 阻塞等待一个信号的发生
signal.pause()

while True:
    time.sleep(1)
    print("等待时钟...")
