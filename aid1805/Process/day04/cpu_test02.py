from cpu_test import *
import threading
import time

# 多线程，执行cpu运算测试效率
counts = []

t1 = time.time()
for x in range(10):
    t = threading.Thread(target=count, args=(1, 1))
    t.start()
    counts.append(t)

n = len(counts)
while True:
    for t in counts:
        if not t.is_alive():
            n -= 1
    if n <= 0:
        break
print("Thread cpu", time.time() - t1)


# # 多线程，执行IO操作测试效率
# def io():
#     write()
#     read()

# counts = []

# t2 = time.time()
# for x in range(10):
#     th = threading.Thread(target = io)
#     th.start()
#     counts.append(th)

# n = len(counts)
# while True:
#     for th in counts:
#         if not th.is_alive():
#             n -= 1
#     if n <= 0:
#         break
# print("Thread IO",time.time() - t2)
