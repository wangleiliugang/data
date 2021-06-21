# 练习：names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 让　names 排序：排序的依据是字符串的反序　'moT'  'yrreJ'   'ekipS'   'ekyT'
# L2 = sorted(names, ...)
# 排序后：L2 = ['Spike', 'Tyke', 'Tom', 'Jerry']
names = ['Tom', 'Jerry', 'Spike', 'Tyke']
def fx(name):
    return name[::-1]
L2 = sorted(names, key=fx)   # key=lambda n: n[::-1]
print(L2)


# 写一个函数input_student() 得到学生的姓名，成绩，年龄
# output_student(L) 打印学生信息
# L = input_student()    # 输入一些学生信息
# print("按年龄从大到小排序后")
# L2 = sorted(L, ...)
# output_student(L2)
# print("按成绩从高到低排序后")
# L3 = sorted(L, ...)
# output_student(L3)

def input_student():
    L= []
    while True:
        n = input("请输入姓名：")
        if not n:
            break
        s = input('请输入成绩：')
        a = input("请输入年龄：")
        d = {}
        d['name'] = n
        d['score'] = s
        d['age'] = a
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

print("按年龄从大到小排序后")
def get_age(d):
    return d['age']
L2 = sorted(L, key=get_age, reverse=True)
output_student(L2)

print("按成绩从高到低排序后")
L3 = sorted(L, key=lambda d: d['score'], reverse=True)
output_student(L3)

# 按字符顺序排序，不区分大小写
def f(ch):
    code = ord(ch)
    if (97+26) > code >= 97:
        code -= 32
    return code
print(sorted('ACDacbdE', key=f))
print(''.join(sorted('ACDacbdE', key=f))) # 重新生成一个字符串









