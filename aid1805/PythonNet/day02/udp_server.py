from socket import *
import sys
from time import ctime


# 收集命令行信息(字符串类型)，将参数传进来，作为对应的IP地址和端口号．
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


# 1.创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 设置套接字选项,将端口号设置为立即重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 2.绑定本地IP和端口号
sockfd.bind(ADDR)

# 3.收发消息
while True:
    data, addr = sockfd.recvfrom(BUFFERSIZE)
    print("接收", addr, "消息内容：", data.decode())
    sockfd.sendto(("在 %s 接收到消息" % ctime()).encode(), addr)

# 4.关闭套接字
sockfd.close()
