import threading
from time import ctime, sleep


a = 10


def music(sec):
    print("Listening music...")
    global a
    a = 1000
    sleep(sec)


t = threading.Thread(target=music, name="my thread", args=(2,))
t.start()
print("创建线程", ctime())
sleep(3)
print('a的值为:', a)
t.join()
