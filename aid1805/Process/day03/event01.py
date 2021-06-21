from multiprocessing import Event

# 生成事件对象
e = Event()

# 检测事件对象:如果被设置则返回True，否则返回False
print(e.is_set())

# 设置事件对象[设置后e.wait()则不再阻塞]
e.set()

# 提供事件的阻塞
# e.wait(3)  #可以对wait()函数设置阻塞时间
e.wait()

print("wait1...")

# 清除对事件的设置
e.clear()

e.wait()

print("wait2...")
