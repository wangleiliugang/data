# 修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能：
# 菜单:
# +-------------------------+
# |  (1)添加学生信息          |
# |  (2)查看所有的学生信息     |
# |  (3)修改学生成绩          |
# |  (4)删除学生信息          |
# |  (q)退出                 |
# +-------------------------+
# 请选择：1
# 请输入添加学生信息姓名：...
# 请选择：3
# 请输入修改学生成绩姓名：...
# (要求每个功能都对应一个函数)

def menu():
    print('+-------------------------+')
    print("|%s" % '(1)添加学生信息', ' ' * 9 + '|')
    print("|%s" % '(2)查看所有的学生信息',' ' * 3 + '|')
    print("|%s" % '(3)修改学生成绩',' ' * 9 + '|')
    print("|%s" % '(4)删除学生信息',' ' * 9 + '|')
    print("|%s" % '(q)退出',' ' * 17 + '|')
    print('+-------------------------+')


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
        t = (d['name'].center(13), str(d['age']).center(7), str(d['score']).center(9))
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


# 定义一个主函数，用来获取键盘操作，实现选择功能
def main():
    # 此列表用来存储所有学生的信息的字典
    docs = []
    while True:
        menu()
        s = input('请选择：')
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            modify(docs)
        elif s == '4':
            delete_info(docs)
        elif s == 'q':
            break     # 结束此函数执行，直接退出
        else:
            print('您的输入有误！')


if __name__ == '__main__':
    main()
