from threading import Thread
# python标准库中的队列模块
import queue
import time

# 创建一个队列模型作为商品的仓库
q = queue.Queue()


# 创建自己的线程类,继承自Thread类
class Producer(Thread):
    # 使用父类的__init__方法，此处可以省略不写．
    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(3):
                    count += 1
                    msg = "产品　%d" % count
                    q.put(msg)  # 将产品放入队列
                    print("生产%s" % msg)
            time.sleep(1)


class Customer(Thread):
    def run(self):
        while True:
            if q.qsize() > 20:
                for i in range(2):
                    msg = q.get()  # 从仓库拿到产品
                    print("消费了一个%s" % msg)
            time.sleep(1)


# 创建3个生产者线程
for i in range(3):
    p1 = Producer()
    p1.start()

# 创建5个消费者线程
for i in range(5):
    c1 = Customer()
    c1.start()
