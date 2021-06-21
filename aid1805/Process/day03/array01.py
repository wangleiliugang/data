from multiprocessing import Process, Array
import time
import ctypes


# 生成一个共享内存空间对象
arr = Array('i', [1, 2, 3, 4, 5])


def fun(arr):
    print(arr)
    for i in arr:
        print(i)
    arr[0] = 1000

# 如果val传入一个正数，则表示在共享内存中开辟一个多大的空间，空间中可以存放的数值类型由ctype确定
# arr = Array('i',6)
# arr = Array('f',6)
# arr = Array(ctypes.c_char,6)


p = Process(target=fun, args=(arr,))
p.start()
p.join()

for i in arr:
    print('parent process:', i)
