from cpu_test import *
import time

# 单线程，执行cpu运算测试效率
# t1 = time.time()
# for i in range(10):
#     count(1,1)
# print('line cpu',time.time() - t1)


# 单线程，执行IO操作测试效率
t2 = time.time()
for i in range(10):
    write()
    read()
print('line IO', time.time() - t2)
