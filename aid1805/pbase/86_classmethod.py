# 此示例示意类方法的定义方法和用法

class Car:
    count = 0

    @classmethod
    def gettotalcount(cls):
        '''此方法为类方法,第一个参数cls,代表调用此方法的类'''
        return cls.count

    @classmethod
    def updatecount(cls, number):
        cls.count += number

print(Car.gettotalcount())  # 用类来调用类方法
# Car.count += 1  # 面向对象思想不提倡直接操作属性
Car.updatecount(1)
print(Car.gettotalcount())

c1 = Car  # 创建一个对象
c1.updatecount(100)　　# Car类的实例也可以调用类方法
print(c1.gettotalcount())

