from socket import *


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)


connfd = socket(AF_INET, SOCK_STREAM, 0)
connfd.connect(ADDR)

while True:
    data = input("请输入要发送的消息：")
    if not data:
        break
    connfd.send(data.encode('utf-8'))
    data = connfd.recv(1024)
    print("收到服务器消息：", data.decode('utf-8'))
connfd.close()
