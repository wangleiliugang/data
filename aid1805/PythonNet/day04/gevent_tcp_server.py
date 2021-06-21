# gevent协程服务器模型
import gevent

# monkey脚本插件的使用要在导入socket模块之前;
# 协程的monkey脚本插件，它可以修改socket模块阻塞部分内容
from gevent import monkey
monkey.patch_all()
from socket import *
import sys


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024


s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(20)


# 创建协程事件
def handler(c, addr):
    print("connect from:", addr)
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("recv msg:", data)
        c.send(b"receive your message!")
    c.close()


while True:
    c, addr = s.accept()
    gevent.spawn(handler, c, addr)

s.close()
