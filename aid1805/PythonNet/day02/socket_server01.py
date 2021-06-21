# 创建多进程的udp并发服务器(fork+udp)
from socketserver import *


ADDR = ('127.0.0.1', 8888)


class MyServer(ForkingUDPServer):
    pass


class handler(DatagramRequestHandler):
    # 因为udp是无连接的，所以request的含义不同
    def handle(self):
        print("connect from:", self.client_address)
        # 使用rfile.readline和wfile.write进行消息的收发
        data = self.rfile.readline()
        print("接收到客户端消息：", data.decode())
        self.wfile.write(b"receive message!")


server1 = MyServer(ADDR, handler)
server1.serve_forever()
