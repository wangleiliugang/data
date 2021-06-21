from socket import *
import os
import sys
import signal
import time

FILE_PATH = '/home/tarena/'

class FtpServer(object):

    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        # 获取指定目录下所有的文件列表
        filelist = os.listdir(FILE_PATH)
        # 服务器端确认请求是否可以执行
        if filelist == None:
            self.connfd.send(b'FALL')
        self.connfd.send(b'OK')
        time.sleep(0.1)  # 避免粘包的出现
        for file in filelist:
            # print(file)
            # os.path.isfile('filename'):判断文件是否为普通文件;返回值False表示不是普通文件,True表示普通文件.
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                # print(file)
                self.connfd.send(file.encode())
                time.sleep(0.1)  # 避免粘包的出现
        self.connfd.send("$$$$".encode())
        print("文件列表发送完成！")
        return 0

    def do_get(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'rb')
        except Exception:
            self.connfd.send(b'FALL')
        self.connfd.send(b'OK')
        time.sleep(0.1)
        for line in fd:
            self.connfd.send(line)
        fd.close()
        time.sleep(0.1)
        self.connfd.send(b'$$$$')
        print("文件发送成功！")
        return 0

    def do_put(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'w')
        except Exception:
            self.connfd.send(b'FALL')
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(BUFFERSIZE).decode()
            if data == '$$$$':
                break
            fd.write(data)
        fd.close()
        print("接收文件完成！")
        return 0


def main():
    if len(sys.argv) != 3:
        print("argv is error!")
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen()
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue
        print("connect from:", addr)
        # print("connect from:",connfd.getpeername())

        pid = os.fork()
        if pid < 0:
            print("创建子进程失败！")
            continue
        elif pid == 0:
            sockfd.close()
            # 生成ftp文件服务器的事件对象
            ftp = FtpServer(connfd)
            # 接收客户端请求
            while True:
                data = connfd.recv(BUFFERSIZE).decode()
                if data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
                elif data[0] == 'Q':
                    print('客户端退出！')
                    # 子进程退出
                    sys.exit(0)
        else:
            connfd.close()
            continue


if __name__ == "__main__":
    main()
