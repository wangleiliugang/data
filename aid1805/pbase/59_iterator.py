# 此示例示意用迭代器来访问可迭代对象

# 用while 循环语句来访问如下列表
# L = [2, 3, 5, 7]

# 方法１
def myiter():
    L = [2, 3, 5, 7]
    it = iter(L)
    l1 = len(L)
    while True:
        if l1 <= 0:
            break
        print(next(it))
        l1 -= 1


myiter()


# 方法２
def myiter():
    L = [2, 3, 5, 7]
    it = iter(L)
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            print("迭代完成！")
            break


myiter()


# 有一个集合s = {'唐僧', '悟空', '八戒', '沙僧'}, 打印出集合内的信息
def myiter():
    s = {'唐僧', '悟空', '八戒', '沙僧'}
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            print("遍历结束！")
            break


myiter()
