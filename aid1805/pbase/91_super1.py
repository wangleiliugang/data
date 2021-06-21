# 此示例示意子类对象用super方法显式调用基类的__init__方法

class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def infos(self):
        print("姓名：", self.name)
        print("年龄：", self.age)

class Student(Human):
    def __init__(self, n, a, s=0):
        super().__init__(n, a)  #显式调用父类的__init__方法．
        self.socre = s

    def infos(self):
        super().infos()
        print("成绩：", self.socre)

s1 = Student("小张", 18, 98)
s1.infos()

# h1 = Human("小赵", 20)
# h1.infos()
