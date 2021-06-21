# 基于poll的io多路复用
from socket import *
import select


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 10120))
s.listen(5)

# 文件描述符地图:以每个io对象的fileno为键，io对象为值
fdmap = {s.fileno(): s}

# 1.创建poll对象
p = select.poll()

# 2.添加关注的io(添加对象或者filno都可以)
p.register(s)

while True:
    # 3.监控关注的io
    events = p.poll()
    # print('events:', events)
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connet from:", addr)
            # 将客户端套接字添加关注并添加到字典
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:  # 按位与，判断具体的事件类型;如果是读事件则执行收发操作．
            data = fdmap[fd].recv(1024).decode()
            # 如果客户端退出则不关注，并且从字典中移除
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send("收到了你的消息！".encode())
s.close()
