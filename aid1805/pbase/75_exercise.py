# 1.写程序让用户输入一系列整数，当输入小于0的数时结束输入
#  1)将输入的数字存于列表中
#  2)将列表中的数字写入到文件numbers.txt中
#  (提示：需要将整数转换为字符串或字节串才能存入文件中)
def save_numbers():
    L = []
    while True:
        n = int(input("请输入整数(输入负数退出)："))
        if n < 0:
            break
        L.append(n)
    return L

def write_to_file(lst, filename='numbers.txt'):
    try:
        f = open(filename, 'w')
        for i in lst:
            f.write(str(i))
            f.write('\n')

        f.close()
    except OSError:
        print("打开文件失败！")

if __name__ == '__main__':
    L = save_numbers()
    print(L)
    write_to_file(L)

# 2.写程序，将文件numbers.txt中的整数读入到内存中，重新形成数组组成的列表，计算这些数的最大值，最小值，和他们的和
# 方法1
def read_from_file(filename='numbers.txt'):
    try:
        f = open(filename)
        L = []
        while True:
            s = f.readline()
            if not s:
                break
            s = s.rstrip()
            n = int(s)
            L.append(n)

        f.close()
    except OSError:
        print("打开文件失败！")
    return L

# 方法2
def read_from_file(filename='numbers.txt'):
    L = []
    try:
        f = open(filename)
        try:
            for line in f:  # line绑定末尾带'\n'的字符串
                n = int(line.rstrip())
                L.append(n)
        finally:
            f.close()
    except OSError:
        print("打开文件失败！")
    except ValueError:
        print("读取文件时出错，数据可能不完整！")
    return L

if __name__ == '__main__':
L = read_from_file()
print(L)
print(max(L), min(L), sum(L))

# 3.为学生信息管理项目添加两个功能：
# 　9) 保存信息到文件(si.txt)
# 10) 从文件中读取数据(si.txt)
# (建议：以行为单位存储数据，用空格或者逗号作为姓名，年龄和成绩的分隔符)
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

def save_info_to_file(lst, filename='si.txt'):
    try:
        f = open(filename, 'w')
        for d in lst:
            f.write(d['name'])
            f.write(',')
            f.write(d['age'])
            f.write(',')
            f.write(d['score'])
            f.write('\n')
        f.close()
    except OSError:
        print("打开文件失败！")

if __name__ == '__main__':
    L = input_student()
    print(L)
    save_info_to_file(L)


def read_info_from_file(filename='si.txt'):
    try:
        f = open(filename)
        L = []
        while True:
            s = f.readline()
            if not s:
                break
            s = s.rstrip()
            name, age, score = s.split(',')
            d = {}
            d['name'] = name
            d['age'] = age
            d['score'] = score
            L.append(d)
        f.close()
    except OSError:
        print("打开文件失败！")
    return L

L = read_info_from_file()
print(L)