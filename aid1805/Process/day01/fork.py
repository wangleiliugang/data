# os模块提供了大量和系统相关的功能函数接口
# os模块的使用是和系统相关的，在不同的系统中可能使用方法不同
import os


print("before create process")
a = 10

# 创建新的进程
pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("This is the new process")
    print(a)
    a = 1000
    print(a)
else:
    print("This is the parent process")
    print(a)

print("The process end")
