import os


pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("child process:")
    print("当前子进程的PID:", os.getpid())
    print("当前进程的父进程PID:", os.getppid())
else:
    print("parent process:")
    print("pid:", pid)
    print("当前父进程的PID:", os.getpid())
