# -*- coding: utf-8 -*-


# 双向队列演示
import collections
import threading
# from multiprocessing import Process
import time

# 创建双向队列
candle = collections.deque("candle")


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
            time.sleep(0.1)
        except IndexError:
            break
        else:
            print('%s : %s\n' % (direction, next))
    print("Done %s \n" % direction)


# 创建两个线程，分别从两端去双向队列中取值。
# 观察是否有异常发生？
tleft = threading.Thread(target=burn, args=('left', candle.popleft))
tright = threading.Thread(target=burn, args=('right', candle.pop))

# 创建两个进程，分别从两端去双向队列中取值。
# tleft = Process(target=burn, args=('left', candle.popleft))
# tright = Process(target=burn, args=('right', candle.pop))

tleft.start()
tright.start()

tleft.join()
tright.join()
