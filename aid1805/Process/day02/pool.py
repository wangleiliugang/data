import os
import multiprocessing as mp
from time import sleep


def worker(msg):
    sleep(2)
    print(msg)
    return "woeker return:" + msg


# 创建进程池对象，processes参数表示进程池中包含4个进程
pool = mp.Pool(processes=4)

result = []
for i in range(10):
    msg = "hello %d" % i
    # 向进程池中加入要执行的事件
    r = pool.apply_async(worker, (msg,))
    # r = pool.apply(worker, (msg,))
    # 使用append接收事件函数的返回值对象．
    result.append(r)

# 获取每个事件函数的返回值
for res in result:
    print('返回值:', res.get())

# 关闭进程池事件加入通道，即不能再向进程池中加入事件
pool.close()
# 必要步骤，阻塞等待进程池处理事件结束后回收进程池
pool.join()
