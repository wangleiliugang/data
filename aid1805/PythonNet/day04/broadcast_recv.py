from socket import *


HOST = ''
PORT = 10120
BUFFERSIZE = 1024


# 创建数据报套接字
s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字为允许广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 绑定IP和端口
s.bind((HOST, PORT))

while True:
    try:
        msg, addr = s.recvfrom(BUFFERSIZE)
        print("get message from:", addr)
        print("广播通知：", msg.decode())
        s.sendto("已经收到广播了！".encode(), addr)
    except Exception as e:
        print("异常信息：", e)
s.close()
