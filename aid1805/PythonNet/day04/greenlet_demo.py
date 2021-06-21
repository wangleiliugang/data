from greenlet import greenlet


# 构建协程函数
def test1():
    print('11111111')
    gr2.switch()
    print('22222222')
    gr2.switch()


def test2():
    print('33333333')
    gr1.switch()
    print('44444444')


# 将函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 选择执行对应的跳转操作
gr1.switch()
