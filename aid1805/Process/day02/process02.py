# 进程函数的使用
from multiprocessing import Process
from time import sleep


a = 1


def worker(sec, msg):
    # 当worker作为子进程运行时，对全局变量a的修改只会影响在子进程中a的值，对父进程没有影响
    global a
    a = 1000
    for i in range(3):
        sleep(sec)
        print("the worker msg:", msg)
    print("child a:", a)


p = Process(name='myworker', target=worker, args=(2,), kwargs={'msg': 'running man!'})

# print("进程名称：", p.name)
# print("进程PID：", p.pid)
# print("进程状态：", p.is_alive())

p.start()

print("进程名称：", p.name)
print("进程PID：", p.pid)
print("进程状态：", p.is_alive())

p.join()
print("parent a:", a)
