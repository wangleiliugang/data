# 自定义一个Mylist类，与系统内建的类一样，用来保存有先后顺序关系的数据

class Mylist:
    def __init__(self, iterator=()):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "Mylist(%r)" % self.data

    def __abs__(self):
        # return Mylist([abs(x) for x in self.data])
        # 上一句语句可以用如下生成器表达式代替以防止过多的占用内存
        return Mylist((abs(x) for x in self.data))

    def __len__(self):
        # return self.data.__len__()
        return len(self.data)

myl = Mylist([1, -2, 3, -4])
print(myl)
print(abs(myl))
print("原来的列表是:", myl)

myl2 = Mylist(range(10))
print(myl2)
print('myl2的长度是:', len(myl2))
print('myl的长度是:', len(myl))
