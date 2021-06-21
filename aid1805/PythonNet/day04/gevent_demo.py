import gevent


# 1.构建协程函数
def foo(a, b):
    print("running in foo", a, b)
    gevent.sleep(3)  # 模拟遇到io阻塞的情况
    print("switch to foo again")


def bar():
    print("running in bar")
    gevent.sleep(2)
    print("switch to bar again")


# 2.将函数注册为协程事件
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

# 3.主进程阻塞等待，回收协程
# gevent.join(f)
# gevent.join(b)
gevent.joinall([f, b])
