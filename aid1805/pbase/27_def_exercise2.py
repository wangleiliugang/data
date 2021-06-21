# 修改之前的学生信息管理系统程序：编写两个函数用于封装　录入学生信息　和　打印学生学生信息的功能
#　1.def input_student():     此函数获取学生信息，并返回学生信息的字典的列表
#　2.def output_student():    以表格形式打印学生信息
#　验证测试：
#   L = input_student()
#   output_student(L)
#   print("再添加几个学生信息")
#   L += input_student()
#   print("添加学生后的学生信息如下：")
#   output_student(L)

def input_student():
    L = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = input("请输入年龄：")
        score = input("请输入成绩：")
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def output_student(L):
    print('+-------------+-------+---------+')
    print('|    name     |  age  |  score  |') 
    print('+-------------+-------+---------+')
    for d in L:
        t =(d['name'].center(13), str(d['age'].center(7)), str(d['score']).center(9))
        line = "|%s|%s|%s|" % t
        print(line)
    print('+-------------+-------+---------+')

L = input_student()
output_student(L)
print("再添加几个学生信息")
L += input_student()
print("添加学生后的学生信息如下：")
output_student(L)


