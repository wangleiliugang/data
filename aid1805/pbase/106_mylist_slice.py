# 此示例示意Slice构造函数

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __getitem__(self, i):
        print("__getitem__被调用，i=", i)
        if type(i) is int:
            print("正在做索引操作")
        elif type(i) is slice:
            print("正在做切片操作")
            print("切片的起始值：", i.start)
            print("切片的终止值：", i.stop)
            print("切片的步长：", i.step)
        else:
            raise KeyError
        return self.data[i]

L1 = MyList([1, -2, 3, -4, 5, -6])
print(L1[::2])  # 等同于调用L1[slice(None, None, 2)]

