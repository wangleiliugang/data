# 此示例示意 __init__方法的自动调用及添加实例变量

# class Car:
#     def __init__(self, c, b, m):
#         # print("__init__方法被调用")
#         self.color = c
#         self.brand = b
#         self.model = m
#         # return None    #通常不需要返回值
    
#     def run(self, speed):
#         print(self.color, '的', self.brand, self.model, '正在以', speed, '码的速度行使！')

#     def set_color(self, clr):
#         '''此方法用来修改车的颜色信息'''
#         self.color = clr
# a4 = Car('红色', '奥迪', 'A4')
# a4.run(179)
# # a4.color = '黑色'
# a4.set_color('黑色')
# a4.run(300)


# 练习：修改之前的Student类
# 1) 为该类添加初始化方法，实现在创建对象时自动设置'姓名'，'年龄'，'成绩'属性
# 2) 添加set_score方法能为对象修改成绩信息
# 3) 添加show_info方法打印学生对象的信息
class Student:
    def __init__(self, n, a=0, s=0):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self, scr):
        self.score = scr

    def show_info(self):
        print('姓名：', self.name, '年龄：', self.age, '成绩：', self.score)

s1 = Student('小张', 21, 98)
s1.set_score(96)
s1.show_info()

s2 = Student('小李', 21)
s2.show_info()
