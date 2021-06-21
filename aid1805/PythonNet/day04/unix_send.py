from socket import *
from time import sleep


BUFFERSIZE = 1024
address = './sockfile01'


s = socket(AF_UNIX, SOCK_STREAM)

try:
    s.connect(address)
except error as e:  # error是socket模块中的错误类
    print("异常信息：", e)

while True:
    try:
        msg = b"this is a unix message!"
        s.send(msg)
        sleep(2)
        data = s.recv(BUFFERSIZE).decode()
        print("receive:", data)
    except error as e:
        print("异常：", e)

s.close()
