import threading
from time import sleep


s = None
e = threading.Event()


def bar():
    print("呼叫foo")
    global s
    s = "天王盖地虎"


def foo():
    print("foo等bar口令")
    sleep(2)
    print("foo收到:%s" % s)
    e.set()  # 将e变为设置的状态


def fun():
    sleep(1)
    e.wait()  # 如果e被设置则不会阻塞，未被设置则阻塞
    print("内奸出现")
    global s
    s = "小鸡炖蘑菇"
    print('内奸修改口令为:', s)


t1 = threading.Thread(target=bar, name='bar')
t2 = threading.Thread(target=foo, name='foo')
t3 = threading.Thread(target=fun, name='fun')

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
