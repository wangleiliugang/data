from multiprocessing import Process, Lock
import time, sys


# 所有进程对临界资源都做加锁操作，程序之间才有影响．
def worker1(stream):
    lock.acquire()  # 加锁
    for i in range(5):
        time.sleep(1)
        stream.write("Lock acquire via\n")
    lock.release()  # 解锁

# def worker2(stream):
#     lock.acquire()
#     for i in range(5):
#         time.sleep(1)
#         stream.write("Lock acquire directly\n")
#     lock.release()


def worker2(stream):
    with lock:  # 加锁，语句块结束即自动解锁
        for i in range(5):
            time.sleep(1)
            stream.write("Lock acquire directly\n")


lock = Lock()
# sys.stdout为所有进程都拥有的资源
p1 = Process(target=worker1, args=(sys.stdout,))
p2 = Process(target=worker2, args=(sys.stdout,))

p1.start()
p2.start()

p1.join()
p2.join()
