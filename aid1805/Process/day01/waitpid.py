import os, sys
from time import sleep


pid = os.fork()

if pid < 0:
    print("create new process failed")
elif pid == 0:
    print("child process...")
    sleep(2)
    sys.exit(6)
else:
    # waitpid非阻塞等待子进程的退出
    p, status = os.waitpid(-1, os.WNOHANG)
    print(p, status)
    print(os.WEXITSTATUS(status))
    print("parent process...")
