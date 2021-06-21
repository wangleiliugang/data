from socket import *
import sys


# 从命令行传入服务器的IP和端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

# 1.创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 2.收发消息
while True:
    data = input("发送消息：")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(BUFFERSIZE)
    print("从服务器接收到消息：", msg.decode())
    print('addr:', addr)

# 3.关闭套接字
sockfd.close()
