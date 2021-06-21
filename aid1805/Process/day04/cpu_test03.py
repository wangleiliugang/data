from cpu_test import *
import multiprocessing
import time

# 多进程，执行cpu运算测试效率
# counts = []

# t1 = time.time()
# for x in range(10):
#     th = multiprocessing.Process(target = count,args = (1,1))
#     th.start()
#     counts.append(th)

# n = len(counts)
# while True:
#     for th in counts:
#         if not th.is_alive():
#             n -= 1
#     if n <= 0:
#         break
# print("Process cpu",time.time() - t1)


# 多进程，执行IO操作测试效率
def io():
    write()
    read()


counts = []
t2 = time.time()
for x in range(10):
    th = multiprocessing.Process(target=io)
    th.start()
    counts.append(th)

n = len(counts)
while True:
    for th in counts:
        if not th.is_alive():
            n -= 1
    if n <= 0:
        break
print("Process IO", time.time() - t2)
