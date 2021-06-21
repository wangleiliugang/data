from multiprocessing import Queue


# 创建消息队列对象
q = Queue(3)

# 存放消息
# q.put('hello1')
# q.put('hello2')
# q.put('hello3')
i = 0
while True:
    # 判断队列是否满了
    if q.full():
        print("queue is full!")
        break
    q.put('hello' + str(i))
    i += 1

print("当前队列有%d条消息" % q.qsize())

for i in range(q.qsize()):
    print("获取消息内容为：%s" % q.get())

print(" Queue is empty?", q.empty())

# print(q.get(False))  # 表示不阻塞
# print(q.get(True,3))  # 表示超时等待时间为3秒
