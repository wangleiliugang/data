# 面向对象的综合示例
# 有两个人: 1.姓名：张三　　　　年龄：35
#          2.姓名：李四　　　　年龄：12
# 行为：1.教别人学东西　teach
#      2.赚钱
#      3.借钱
# 事情：张三　教　李四　学 python
#      李四　教　张三　学　跳绳
#      张三　上班赚了　1000元钱
#      李四　向张三　借了　200元钱


# 此示例示意如何用面向对象的方式创建对象，并建立对象与对象之间的逻辑关系
class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.money = 0

    def teach(self, other, skill):
        print(self.name, '教', other.name, '学', skill)

    def works(self, money):
        self.money += money
        print(self.name, '上班赚了', money, '元钱')

    def borrow(self, other, money):
        if other.money > money:
            print(other.name, "借给", self.name, money, '元钱')
            other.money -= money
            self.money += money
        else:
            print(other.name, '钱不够！')

    def show_info(self):
        print(self.age, '岁的', self.name, '有存款：', self.money, '元钱')

zhang3 = Human('张三', 35)
li4 = Human('李四', 12)
zhang3.teach(li4, 'python')
li4.teach(zhang3, '跳绳')
zhang3.works(1000)
li4.borrow(zhang3, 200)
# li4.borrow(zhang3, 2000)  # 钱不够，无法借钱！
zhang3.show_info()
li4.show_info()

