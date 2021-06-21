from socket import *
from multiprocessing import Process
import os
import sys


# 有客户端断开则关闭相应的子进程
def handler(c):
    s.close()
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到：", data)
        c.send(b"receive your message")
    c.close()


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

# 1.创建套接字　绑定　监听
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 2.接收客户端连接请求，创建新的进程
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        print("服务器结束！")
        s.close()
        os._exit(0)
    except Exception:
        continue
    print("接收到客户端连接：", c.getpeername())

    # 创建子进程处理客户端事件，通过传参的方式将c变成局部变量
    p = Process(target=handler, args=(c,))
    p.deamon = True  # 主进程执行完毕其它进程也终止执行
    p.start()
# 3.主进程继续接收下一个客户端连接请求
c.close()
