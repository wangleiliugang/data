# 此示例示意布尔测试函数的重写

class Mylist:
    def __init__(self, iterator=()):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "Mylist(%r)" % self.data

    # def __bool__(self):
    #     print("__bool__方法被调用！")
    #     return False

    # def __len__(self):
    #     print("__len__被调用！")
    #     return len(self.data)

myl = Mylist([1, -2, 3, -4])
print(bool(myl))
if myl:
    print("myl是真值！")
else:
    print("myl是假值！")
