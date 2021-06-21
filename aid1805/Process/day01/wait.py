import os, sys
from time import sleep


pid = os.fork()

if pid < 0:
    print("create new process failed")
elif pid == 0:
    print("child process...")
    sleep(2)
    sys.exit(6)  # 子进程退出
else:
    # wait 阻塞父进程运行，等待子进程的退出
    p, status = os.wait()
    print('退出的子进程的PID号:', p, ';子进程的退出状态:', status)
    print(os.WEXITSTATUS(status))  # 可以打印出子进程的退出码
    print("parent process...")
    while True:
        pass
