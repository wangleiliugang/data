# python网络套接字模块
from socket import *


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


# 1.创建一个tcp流式套接字
sockfd = socket(AF_INET, SOCK_STREAM, 0)

# 2.绑定本机的IP和端口号
sockfd.bind(ADDR)

# 3.将套接字变为可监听的套接字
sockfd.listen(5)
print("wait for connect...")

# 4.套接字等待客户端请求(返回的参数代表：和客户端交互的新的套接字;连接进来的客户端的地址address)
conn, addr = sockfd.accept()
print("connect from:", addr)

# 5.消息的收发(python3中要求recv接收/send发送的内容必须为bytes格式)
data = conn.recv(BUFFERSIZE)
print("接收到客户端消息：", data.decode('utf-8'))
n = conn.send("recv your message\n".encode('utf-8'))
print("发送了　%d　字节的数据" % n)

# 6.关闭套接字
conn.close()       # 表示和客户端断开连接
sockfd.close()     # 表示不能再使用sockfd套接字
