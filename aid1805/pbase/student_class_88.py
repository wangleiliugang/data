# 练习：用类来描述一个学生的信息(可以修改之前写的Student类)
# class Student:
#     此处自己实现
# 要求该类的对象用于存储学生信息：姓名，年龄，成绩
# 将这些对象存于列表中，可以任意添加和删除学生信息
# 1.打印出学生的个数
# 2.打印出所有学生的平均成绩
# (建议用类变量存储学生的个数，也可以把列表当作类变量)

class Student:
    count = 0  # 此类变量用来记录学生的个数

    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s
        Student.count += 1  # 让对象个数加1

    def __del__(self):
        Student.count -= 1  # 对象销毁时类个数减1

    def get_score(self):
        return self.score

    @classmethod
    def gettotalcount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count

def test():
    L = []  # 1班学生
    L.append(Student('小张', 20, 100))
    L.append(Student('小王', 18, 96))
    L.append(Student('小李', 19, 98))
    print("此时学生对象的个数是：", Student.gettotalcount())

    L2 = []  # 2班学生
    L2.append(Student('小赵', 18, 99))
    print("此时个数是：", Student.gettotalcount())
    # 删除L中的一个学生
    L.pop(1)
    print("此时学生个数是：", Student.gettotalcount())

    all_student = L + L2
    scores = 0  # 用此变量来记录所有学生的成绩总和
    for s in all_student:
        # scores += s.score  # 累加所有学生的成绩
        scores += s.get_score()

    print("平均成绩是：", scores/len(all_student))


if __name__ == '__main__':
    test()

