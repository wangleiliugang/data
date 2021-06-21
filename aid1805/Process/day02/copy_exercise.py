import os


# 获取文件的大小
size = os.path.getsize('fork.py')

pid = os.fork()

if pid < 0:
    print("创建进程失败！")
# 子进程拷贝前半部分
elif pid == 0:
    n = size // 2
    fw = open('child file', 'w')
    with open('fork.py') as f:
        while True:
            if n < 64:
                data = f.read(n)
                fw.write(data)
                break
            data = f.read(64)
            fw.write(data)
            n -= 64
    fw.close()

# 父进程拷贝后半部分
else:
    fw = open('parent file', 'w')
    with open('fork.py') as f:
        f.seek(size // 2, 0)
        while True:
            data = f.read(64)
            if not data:
                break
            fw.write(data)
    fw.close()
