# 此示例示意为属性和方法结合在一起使用

# class Dog:
#     def eat(self, food):
#         print(self.color, '的', self.kinds, '正在吃', food)


# # 创建第一个对象
# dog1 = Dog()
# dog1.kinds = '京巴'  # 添加属性kinds
# dog1.color = '白色'  # 添加属性color
# # print(dog1.color, '的', dog1.kinds)  # 访问属性
# dog1.eat("骨头")

# dog2 = Dog()
# dog2.kinds = '牧羊犬'
# dog2.color = '灰色'
# # print(dog2.color, '的', dog2.kinds)
# dog2.eat("包子")


# 练习
# 定义一个学生类：
class Student:
    def set_info(self, name, age=0):
        '''此方法用来给学生对象添加＇姓名＇和＇年龄＇属性'''
        self.name = name
        self.age = age

    def show_info(self):
        '''此处显示此学生的信息'''
        print(self.name, '今年', self.age, '岁')

s1 = Student()
s1.set_info('小张', 20)
s2 = Student()
s2.set_info('小李', 18)
s1.show_info()     # 小张　今年　20　岁
s2.show_info()     # 小李　今年　18　岁
