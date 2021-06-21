from socket import *
import time


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(5)

# 将sockfd变为非阻塞，默认是True
sockfd.setblocking(False)

# 设置sockfd的超时时间
# sockfd.settimeout(5)

while True:
    print("wait for connect...")
    # time.sleep(10)
    try:
        conn, addr = sockfd.accept()
        print("connect from:", addr)
        # conn.setblocking(False)  # 将recv设置为非阻塞状态
        while True:
            data = conn.recv(BUFFERSIZE)
            if not data:
                break
            print("接收到客户端消息：", data.decode())
            n = conn.send("recv your message\n".encode())
            print("发送了　%d　字节的数据" % n)
        conn.close()
    except Exception as e:
        print('异常信息:', e)
sockfd.close()
