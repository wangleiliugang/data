from socket import *


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.bind(ADDR)
sockfd.listen(5)

# 循环接收客户端请求连接
while True:
    print("server:wait for connect...")
    conn, addr = sockfd.accept()
    print("connect from:", addr)
    # 循环收发客户端消息
    while True:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print("接收到客户端消息：", data.decode('utf-8'))
        n = conn.send("recv your message.\n".encode('utf-8'))
        print("发送了　%d　字节的数据" % n)
    conn.close()
sockfd.close()
