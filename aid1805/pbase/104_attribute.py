# 此示例示意对象的属性管理函数

# class Dog:
#     pass

# dog1 = Dog()
# # print(dog1.color)  # 会出错，对象没有这个属性
# print(getattr(dog1, 'color', '没有颜色'))  # 没有颜色
# print(hasattr(dog1, 'color'))
# dog1.color = '白色'
# print(getattr(dog1, 'color', '没有颜色'))  # 白色
# print(hasattr(dog1, 'color'))

# setattr(dog1, 'kinds', '田园犬')  # dog1.kinds = '田园犬'
# print(getattr(dog1, 'kinds', '没有种类'))
# # print(getattr(dog1, 'color', None))


# 练习
# 写一个Car类，属性有：颜色--->color，　品牌--->brand
class Car:
    def __init__(self, c, b):
        self.color, self.brand = c, b

    # 添加一个方法
    def get_car_attr(self, attr_name):
        '''此方法用于获取对象的属性，如果属性名attr_name在此对象内不存在则返回 None'''
        return getattr(self, attr_name, None) 

c1 = Car('黑色', 'Benz')
v = c1.get_car_attr('color')
# try:
#     v = c1.__dict__['color']
# except KeyError:
#     v = None

if v is None:
    print("没有颜色属性")
else:
    print("颜色是：", v)





