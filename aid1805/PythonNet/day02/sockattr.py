from socket import *


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

sockfd = socket(AF_INET, SOCK_STREAM)
print("套接字的属性：", sockfd.type)
print("sockfd的文件描述符编码：", sockfd.fileno())

# 将端口号设置为立即重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print("获取选项值：", sockfd.getsockopt(SOL_SOCKET, SO_REUSEADDR))

sockfd.bind(ADDR)
sockfd.listen(5)
print("套接字的地址和端口：", sockfd.getsockname())

while True:
    print("wait for connect...")
    conn, addr = sockfd.accept()
    # 使用getpeername()获取连接的客户端的地址
    print("connect from:", conn.getpeername())
    while True:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print("接收到客户端消息：", data.decode())
        n = conn.send("recv your message\n".encode())
        print("发送了 %d 字节的数据" % n)
    conn.close()
sockfd.close()
