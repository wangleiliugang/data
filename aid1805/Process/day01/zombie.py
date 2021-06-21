import os
import time


pid = os.fork()

if pid < 0:
    print("create new process failed")
elif pid == 0:
    print("子进程退出了")
    os._exit(0)
else:
    time.sleep(1)
    print("子进程的PID:", pid)
    while True:
        pass
