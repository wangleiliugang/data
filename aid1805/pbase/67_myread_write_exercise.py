# 1.写一个程序，从键盘输入如下信息：
# 姓名　和　电话号码
# 如: 请输入姓名：xiaozhang
#     请输入电话：13888888888
#     请输入姓名：xiaoli
#     请输入电话：13999999999
#     请输入姓名：<回车>
# 把从键盘读取的信息存入'phone_book1.txt'文件中，然后用sublime text打开并查看写入的内容

def phone_number():
    L = []
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        number = input("请输入电话：")
        d = {}
        d['name'] = name
        d['number'] = number
        L.append(d)
    return L

def write_to_file(lst, filename='phone_book1.txt'):
    try:
        f = open(filename, 'w')
        for d in lst:
            f.write(d['name'])
            f.write(',')
            f.write(d['number'])
            f.write('\n')
        f.close()
    except OSError:
        print("打开文件失败！")

if __name__ == '__main__':
    L = phone_number()
    print(L)
    write_to_file(L)


# 2.写一个读取'phone_book1.txt'文件的程序，把保存的信息以表格的形式打印出来
#   +-------------+-------------------+
#   |     name    |     number        |
#   +-------------+-------------------+
#   |  xiaozhang  |    13888888888    |
#   +-------------+-------------------+
def read_info_from_file(filename='phone_book1.txt'):
    L = []
    try:
        f = open(filename)
        while True:
            s = f.readline()
            if not s:
                break
            s = s.rstrip()
            name, number = s.split(',')
            d = {}
            d['name'] = name
            d['number'] = number
            L.append(d)
        f.close()
    except OSError:
        print("打开文件失败！")
    return L

def print_info(lst):
    print('+-------------+-----------------------+')
    print('|    name     |         number        |') 
    print('+-------------+-----------------------+')
    for d in L:
        t =(d['name'].center(13), d['number'].center(23))
        line = "|%s|%s|" % t
        print(line)
    print('+-------------+-----------------------+')

if __name__ == '__main__':
    L = read_info_from_file()
    print(L)
    print_info(L)

