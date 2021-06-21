# 练习：修改之前的学生管理系统
# 原学生数据使用字典存储，现改为用对象进行存储，要求自定义Student类来封装学生的信息和行为

# file: student_exercise.py
class Student:
    count = 0  # 此类变量用来记录学生的个数
    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1  # 让对象个数加1

    def __del__(self):
        Student.count -= 1  # 对象销毁时类个数减1

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return
        raise ValueError('不合法的成绩信息' + str(score))

    def get_infos(self):
        return (self.__name, self.__age, self.__score)

    def is_name(self, n):
        '''判断n是否和self的名字相同'''
        return self.__name == n

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')

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