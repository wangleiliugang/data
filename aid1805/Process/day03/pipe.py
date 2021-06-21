from multiprocessing import Process, Pipe
import os, time


# 创建管道对象
# 当参数为False的时候child只能recv，parent只能send
# child_conn,parent_conn = Pipe(False)
child_conn, parent_conn = Pipe()


# 创建子进程函数
def fun(name):
    time.sleep(2)
    # 发送一个字符串到管道
    child_conn.send("hello" + str(name))
    print(os.getppid(), '----->', os.getpid())


lst = []
# 创建5个子进程
for i in range(5):
    p = Process(target=fun, args=(i,))
    lst.append(p)
    p.start()

# 父进程从管道中接收数据
for i in range(5):
    data = parent_conn.recv()
    print('parent_recv:', data)

for i in lst:
    i.join()
