from socket import *
import os


# 1.设置通信的套接字文件
address = './sockfile01'

# 2.判断套接字文件是否存在
try:
    os.unlink(address)  # 删除当前目录下的sockfile01文件
except OSError:
    # 判断文件是否删除存在,如果address存在,返回True;如果address不存在,返回False
    if os.path.exists(address):
        raise
    else:
        pass

# 3.创建本地套接字
s = socket(AF_UNIX, SOCK_STREAM)
# 绑定本地套接字的文件
s.bind(address)
s.listen(5)

while True:
    conn, addr = s.accept()
    print("connect from:", addr)  # addr是空字串
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("receive:", data)
        conn.send(b"receive your message!")
    conn.close()
s.close()
