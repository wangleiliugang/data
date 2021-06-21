# 基于select的io多路复用监听服务器
from socket import *
import select  # io多路复用模块
import time
import sys


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

# s套接字作为一个io事件
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    # 监听3个关注列表中的io事件
    rs, ws, es = select.select(rlist, wlist, xlist)
    print("有io事件发生了...")
    # 通过for循环遍历每个返回列表，去处理io事件
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from:", addr)
            # 将新的io事件加入到监控列表
            rlist.append(c)
            xlist.append(c)
        else:
            # 因为rs列表中可能有很多c属性，用r对象可以很好的区分开
            data = r.recv(1024).decode()
            if not data:
                print("有客户端退出！")
                rlist.remove(r)
                xlist.remove(r)
                r.close()
                continue
            else:
                # 需要服务器主动处理事情时，将r对象添加到ws列表中
                wlist.append(r)
            print("收到客户端消息:", data, r.getpeername(), time.ctime())
    for w in ws:
        # 主动处理的io事件
        w.send("服务器收到了你的消息。".encode())
        wlist.remove(w)
    for e in es:
        if e is s:
            s.close()
            sys.exit(0)
        else:
            rlist.remove(e)
            xlist.remove(e)
            e.close()
