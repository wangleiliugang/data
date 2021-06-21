import multiprocessing as mp
from time import sleep


def fun():
    print("child process start")
    sleep(3)
    print("child process end")


p = mp.Process(target=fun)

# 默认值为False，表示主进程运行结束后不会影响子进程的运行，直到子进程运行完进程才会结束;
# 如果设置为True，主进程运行完毕后所有子进程也不再运行一起退出
# p.daemon = False
p.daemon = True
p.start()
# p.join()
sleep(1)
print("******main process over******")
