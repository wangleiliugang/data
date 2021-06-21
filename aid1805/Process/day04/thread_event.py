from threading import *
import random
from time import sleep


a = 500
# 创建事件对象
e = Event()


# 分支线程不断减少a，以确保a不超过200
def fun():
    global a
    while True:
        sleep(2)
        print('a=', a)
        e.wait()  # 如果e被设置则不会阻塞，未被设置则阻塞
        a -= random.randint(0, 100)


t = Thread(target=fun)
t.start()

# 主线程不断的让a增加，但是a不超过200
while True:
    sleep(1)
    a += random.randint(1, 10)
    print('主线程中打印a:', a)
    if a > 200:
        e.set()
    else:
        e.clear()

t.join()
