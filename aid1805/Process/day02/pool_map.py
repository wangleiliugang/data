from multiprocessing import Pool
import time


def fun(fn):
    time.sleep(1)
    return fn * fn


lst = [1, 2, 3, 4, 5, 6]

print("顺序执行")
t1 = time.time()
for i in lst:
    fun(i)
t2 = time.time()
print("执行时间为：", t2 - t1)
print('-' * 20)


print("进程池执行")
pool = Pool(processes=8)
r = pool.map(fun, lst)
pool.close()
pool.join()
print("执行时间为：", time.time() - t2)
