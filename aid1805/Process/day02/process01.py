import multiprocessing as mp
import os
import time


def th1():
    print(os.getppid(), '-----', os.getpid())
    print('吃早饭')
    time.sleep(1)
    print('吃午饭')
    time.sleep(2)
    print('吃晚饭')
    time.sleep(3)


def th2():
    print(os.getppid(), '-----', os.getpid())
    print("中午睡觉")
    time.sleep(1)
    print("晚上睡觉")
    time.sleep(3)


def th3():
    print(os.getppid(), '-----', os.getpid())
    print("打1号豆豆")
    time.sleep(2)
    print("打2号豆豆")
    time.sleep(2)


# 同一类函数，放在同一个列表中．(函数形参一致)
things = [th1, th2, th3]
process = []

for th in things:
    p = mp.Process(target=th)
    process.append(p)

for p in process:
    p.start()

for i in process:
    i.join(0.1)

print('***********')

# 创建子进程，生成子进程对象
# p1 = mp.Process(target = th1)
# p2 = mp.Process(target = th2)
# p3 = mp.Process(target = th3)

# p1.start()
# p2.start()
# p3.start()

# p1.join()
# p2.join()
# p3.join()
