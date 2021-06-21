from socket import *
import sys


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

connfd = socket(AF_INET, SOCK_STREAM)
connfd.connect(ADDR)

while True:
    data = input("请输入要发送的消息：")
    if not data:
        break
    connfd.send(data.encode('utf-8'))
    data = connfd.recv(1024)
    print("服务器：", data.decode('utf-8'))
connfd.close()
