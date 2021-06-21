from socket import *


# 要连接的服务器的地址信息
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


# 1.创建客户端套接字，要和访问的服务器的套接字类型相同
connfd = socket(AF_INET, SOCK_STREAM, 0)

# 2.连接服务器
connfd.connect(ADDR)

# 3.和服务器进行通信(python3中要求recv接收/send发送的内容必须为bytes格式)
# connfd.send(b"hello!")
# connfd.send("hello!".encode("utf-8"))
connfd.sendall(b"hello!")
data = connfd.recv(BUFFERSIZE)
print("收到服务器消息：", data.decode('utf-8'))

# 4.关闭套接字，同时会和服务器断开连接
connfd.close()
