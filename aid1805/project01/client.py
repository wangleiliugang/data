# 聊天室客户端
from socket import *
import sys
import os
import signal


# 子进程发送消息
def do_child(s, addr, name):
    while True:
        text = input('发言：')
        # 表示用户要退出聊天
        if text == 'quit':
            msg = 'Q##' + name
            s.sendto(msg.encode(), addr)
            # 让父进程结束后，子进程再退出
            os.kill(os.getppid(), signal.SIGKILL)
            sys.exit(0)
        # 正常聊天
        else:
            msg = 'C##%s##%s' % (name, text)
            s.sendto(msg.encode(), addr)


# 父进程接收消息
def do_parent(s):
    while True:
        msg, addr = s.recvfrom(1024)
        # print(msg.decode(), end = '')
        print(msg.decode('utf-8') + '\n发言:', end='')


def main():
    if len(sys.argv) != 3:
        print("argv error!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    # 创建数据报套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    while True:
        name = input("请输入姓名：")
        if not name:
            print('用户名不能为空。')
            continue
        else:
            msg = 'L##' + name
            s.sendto(msg.encode(), ADDR)
            data, addr = s.recvfrom(1024)
            if data.decode() == 'OK':
                break
            else:
                print("用户名已存在！")

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    # 创建进程
    pid = os.fork()
    if pid < 0:
        print("create process failed!")
        return
    elif pid == 0:
        do_child(s, addr, name)
    else:
        do_parent(s)


if __name__ == '__main__':
    main()
