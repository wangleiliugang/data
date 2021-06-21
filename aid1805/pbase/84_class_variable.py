# 此示例示意类变量的定义和使用

# class Human:
#     count = 0

# print('Human的类变量count=', Human.count)  # 0
# Human.count = 100
# print(Human.count)  # 100


# 此示例示意Human类的实例可以访问count类变量

# class Human:
#     count = 0

# print('Human的类变量count=', Human.count)  # 0
# h1 = Human()
# print('用h1对象访问Human的count变量', h1.count)
# h1.count = 100      #在h1实例对象内部创建变量，即实例变量
# print(h1.count)     # 100
# print(Human.count)  # 0

# h1.__class__.count += 1
# print('h1.count=', h1.count)  # 100
# print('Human.count=', Human.count)  # 1


# 此示例示意用类变量来记录对象的个数
class Car:
    count = 0
    def __init__(self, info):
        print(info, "被创建")
        self.data = info  # 记录传入数据
        self.__class__.count += 1  # 让车的总数加1

    def __del__(self):
        print(self.data, "被销毁")
        self.__class__.count -= 1  # 当车被销毁时总数自动减1

print("当前汽车总数是：", Car.count)
b1 = Car("BYD 京A.88888")
print(Car.count)
b2 = Car("TESLA 京B.00000")
b3 = Car("Audi 京C.66666")
print("当前汽车总数是：", Car.count)
del b1
print("当前汽车总数是：", Car.count)
del b2
print("当前汽车总数是：", Car.count)
