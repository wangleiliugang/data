from time import ctime, sleep
import threading


# 编写自己的线程类
class MyThread(threading.Thread):
    def __init__(self, func, args, name='Levi'):
        # threading.Thread.__init__(self)
        super().__init__()
        self.func = func
        self.args = args
        self.name = name

    # 自定义线程启动函数
    def run(self):
        self.func(*self.args)


# 待启动的线程函数
def player(file, time):
    for i in range(2):
        print('start playing%s:%s' % (file, ctime()))
        sleep(time)


t = MyThread(player, ('baby.mp3', 3))
t.start()
t.join()
