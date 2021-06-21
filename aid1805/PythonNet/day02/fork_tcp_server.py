from socket import *
import os
import sys
import signal


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


# 有客户端断开则关闭相应的子进程
def child_handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到：", data)
        c.send(b"receive your message!")
    c.close()
    os._exit(0)


# 1.创建流式(tcp)套接字　绑定　监听
s = socket(AF_INET, SOCK_STREAM)
# 设置端口可以重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen()

# 父进程处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 2.循环接收客户端连接请求，创建新的进程
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        print("服务器结束!")
        s.close()
        os._exit(0)
    except Exception:
        continue
    print("接收到客户端连接：", c.getpeername())

    # 创建进程
    pid = os.fork()
    if pid < 0:
        print("创建子进程失败！")
        continue
    # 子进程处理客户端事件
    elif pid == 0:
        s.close()
        print("开始处理客户端请求...")
        # 处理客户端的函数
        child_handler(c)
    # 主进程继续接收下一个客户端连接请求
    else:
        c.close()
        continue
