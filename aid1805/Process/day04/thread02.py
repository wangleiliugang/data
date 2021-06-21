import threading
from time import sleep, ctime


def fun():
    print("this is a thread test")
    sleep(5)
    print("thread over")


th = threading.Thread(target=fun, name="hai...")

# 设置为True，则主线程执行完毕其它线程也终止执行
# t.setDaemon(True)
th.daemon = True
print(th.isDaemon())

th.start()

print("线程状态：", th.is_alive())
print("线程名称：", th.name)

th.join(2)

print("all over；", ctime())
