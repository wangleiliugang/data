import os
import time


# 创建新的进程
pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("子进程pid:", pid)
    print('ppid', os.getppid())
    while True:
        time.sleep(0.8)
        print("This is the new process")
        # 子进程的退出不会影响父进程
        os._exit(0)
else:
    # 父进程中pid为子进程的PID号
    print("父进程pid:", pid)
    print('pid', os.getpid())
    while True:
        time.sleep(1)
        print("This is the parent process")

print("The process end")
