from student_exercise_83 import Student

def input_student():
    L = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = input("请输入年龄：")
        score = input("请输入成绩：")
        d = Student(name, age, score)
        L.append(d)
    return L

def output_student(L):
    print('+-------------+-------+---------+')
    print('|    name     |  age  |  score  |') 
    print('+-------------+-------+---------+')
    for d in L:
        n, a, s = d.get_infos()
        t =(n.center(13), str(a).center(7), str(s).center(9))
        line = "|%s|%s|%s|" % t
        print(line)
    print('+-------------+-------+---------+')

def modify(L):
    name = input("请输入修改学生姓名：")
    for d in L:
        if d.is_name(name):
            score = int(input("请输入新的成绩："))
            d.set_score(score)
            print('修改', name, '新的成绩为：', score)
            return
    else:
        print('没有找到名为：', name, '的学生信息')

def delete_info(L):
    name = input("请输入删除学生姓名：")
    for i in range(len(L)):
        if L[i].is_name == name:
            del L[i]
            print('删除', name, '的学生信息成功!')
            return True
    else:
        print('没有找到名为：', name, '的学生信息')
def print_by_score_desc(lst):
    L = sorted(lst, key=lambda d:d.get_score(), reverse=True)
    print(L)
    output_student(L)

def print_by_score_asc(lst):
    L = sorted(lst, key=lambda d:d.get_score())
    output_student(L)

def print_by_age_desc(lst):
    L = sorted(lst, key=lambda d:d.get_age(), reverse=True)
    output_student(L)

def print_by_age_asc(lst):
    L = sorted(lst, key=lambda d:d.get_age())
    output_student(L)

def save_to_file(docs, filename='si.txt'):
    try:
        # f = open(filename, 'w')
        f = open(filename, 'a')
        for stu in docs:
            # n, a, s = stu.get_infos
            stu.write_to_file(f)
        f.close()
        print("文件保存成功！")
    except OSError:
        print("文件保存失败！")

def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for line in f:
            s = line.rstrip()  # 去掉右侧的'\n'
            lst = s.split(',')  # ['姓名','年龄','成绩']
            name, age, score = lst
            age = int(age)
            score = int(score)
            L.append(Student(name, age, score))
        f.close()
    except OSError:
        print("文件打开失败！")
    return L

print('student_project_83模块被导入')