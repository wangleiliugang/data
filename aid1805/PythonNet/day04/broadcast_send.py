from socket import *
from time import sleep


BUFFERSIZE = 1024


# 设置发送的广播地址　　<broadcast>
broadcast_address = ('<broadcast>', 10120)
# broadcast_address = ('192.168.1.255',9999)

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    sleep(2)
    s.sendto("同志们开会啦！！！".encode(), broadcast_address)
    data, addr = s.recvfrom(BUFFERSIZE)
    print(data.decode())
s.close()
