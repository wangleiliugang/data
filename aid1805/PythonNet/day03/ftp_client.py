from socket import *
import sys
import time


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        # 发送请求
        self.sockfd.send(b"L")
        # 接收服务器确认 OK or FALL
        data = self.sockfd.recv(BUFFERSIZE).decode()
        if data == 'OK':
            while True:
                data = self.sockfd.recv(BUFFERSIZE).decode()
                if data == '$$$$':
                    break
                print(data)
            print("文件列表接收展示完成！")
            return 0
        else:
            print("文件列表请求失败！")
            return 0

    def do_get(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(BUFFERSIZE).decode()
        if data == 'OK':
            fd = open(filename, 'w')
            while True:
                data = self.sockfd.recv(BUFFERSIZE).decode()
                if data == '$$$$':
                    break
                fd.write(data)
            fd.close()
            print("%s下载完成！" % filename)
            return 0
        else:
            print("下载文件失败！")
            return 0

    def do_put(self, filename):
        try:
            fd = open(filename, 'r')
        except Exception:
            print("上传文件不存在！")
            return 0
        self.sockfd.send(("P " + filename).encode())
        data = self.sockfd.recv(BUFFERSIZE).decode()
        if data == 'OK':
            for line in fd:
                self.sockfd.send((line).encode())
            fd.close()
            time.sleep(0.1)
            self.sockfd.send(('$$$$').encode())
            print("上传文件完成！")
            return 0
        else:
            print("上传文件失败！")
            return 0

    def do_quit(self):
        self.sockfd.send(b"Q")


def main():
    if len(sys.argv) != 3:
        print("argv is error!")
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.connect(ADDR)
    # 生成ftp文件客户端的事件对象
    ftp = FtpClient(sockfd)
    while True:
        print("********命令选项************")
        print("********查看：list**********")
        print("********下载：get filename**")
        print("********上传：put filename**")
        print("********退出：quit**********")
        data = input("请输入命令：")
        if data[:4] == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)
        elif data[:4] == 'quit':
            ftp.do_quit()
            sockfd.close()
            sys.exit(0)
        else:
            print("请输入正确命令！")
            continue


if __name__ == "__main__":
    main()
