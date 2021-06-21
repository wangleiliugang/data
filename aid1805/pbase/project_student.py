
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

def modify(L):
    name = input("请输入修改学生姓名：")
    for d in L:
        if d['name'] == name:
            score = int(input("请输入新的成绩："))
            d['score'] = score
            print('修改', name, '新的成绩为：', score)
            return
    else:
        print('没有找到名为：', name, '的学生信息')

def delete_info(L):
    name = input("请输入删除学生姓名：")
    for i in range(len(L)):
        if L[i]['name'] == name:
            del L[i]
            print('删除', name, '的学生信息成功!')
            return True
    else:
        print('没有找到名为：', name, '的学生信息')
def print_by_score_desc(lst):
    L = sorted(lst, key=lambda d:d['score'], reverse=True)
    print(L)
    output_student(L)

def print_by_score_asc(lst):
    L = sorted(lst, key=lambda d:d['score'])
    output_student(L)

def print_by_age_desc(lst):
    L = sorted(lst, key=lambda d:d['age'], reverse=True)
    output_student(L)

def print_by_age_asc(lst):
    L = sorted(lst, key=lambda d:d['age'])
    output_student(L)

print('project_student模块被导入')