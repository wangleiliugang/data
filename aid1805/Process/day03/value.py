from multiprocessing import Value, Process
import time
import random


# 生成一个共享内存空间对象
money = Value('i', 2000)

# obj.value属性: 获取共享内存中的值
print("共享内存的初始值:", money.value)


def deposite(money):
    for i in range(100):
        time.sleep(0.03)
        money.value += random.randint(1, 200)


def withdraw(money):
    for i in range(100):
        time.sleep(0.02)
        money.value -= random.randint(1, 150)


d = Process(target=deposite, args=(money,))
w = Process(target=withdraw, args=(money,))

d.start()
w.start()

d.join()
w.join()

print("父子进程通信后的值:", money.value)
