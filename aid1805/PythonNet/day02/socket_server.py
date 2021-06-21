# 创建多进程的tcp并发服务器(fork+tcp)
from socketserver import *

ADDR = ('127.0.0.1', 8888)
BUFFERSIZE = 1024


# 1.创建服务器类
# class Myserver(ForkingTCPServer):
class MyServer(ForkingMixIn, TCPServer):
    pass


# 2.创建处理类
class Handler(StreamRequestHandler):
    # 当有客户端连接时，调用该函数自动处理客户端请求事件
    def handle(self):
        print("connect from:", self.client_address)
        while True:
            # self.request为tcp中系统自动生成的与客户端交互的套接字
            data = self.request.recv(BUFFERSIZE).decode()
            if not data:
                break
            print("服务器收到：", data)
            self.request.send("情不知所起，一往而深".encode())


# 3.使用创建的服务器类生成服务器
server1 = MyServer(ADDR, Handler)

# 4.运行服务器
server1.serve_forever()
