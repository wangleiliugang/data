# 此示例示意以文本文件方式读取abc.txt中的数据

try:
    f = open("abc.txt")
    print("文件打开成功！")
    s = f.readline()
    if s != '':
        print("读取成功，文字是：", s)
    else:
        print("文件内没有数据可读！")
    s = f.readline()
    print("第二行数据是：", s)
    s = f.readline()
    print("第三行数据是：", s)
    s = f.readline()
    if s == '':
        print("文件内已经没有数据可读取！")
    else:
        print("第四行文字是：", s)

    f.close()
except OSError:
    print("文件打开失败！")


# 练习：写一个文件info.txt 内部存一些文字信息
#      张三　　20  98
# 　　　　　李四  21  95
#      小王  22  100　
# 写程序将这些数据读取出来，打印在屏幕终端上
#　方法１
def read_info_text():
    try:
        f = open("info.txt")
        while True:
            s = f.readline()
            if s != '':         # if not s:
                print(s)        #     break
            else:               # print(s)
                break
        f.close()
    except OSError:
        print("打开info.txt文件失败！")

if __name__ == '__main__':
    read_info_text()
print('--------------')
#　方法２
def read_info_text():
    try:
        f = open("info.txt")
        while True:
            s = f.readline()
            if s != '':
                if s[-1] == '\n':
                    print(s[:-1])
                else:
                    print(s)
            else:
                break
        f.close()
    except OSError:
        print("打开info.txt文件失败！")

if __name__ == '__main__':
    read_info_text()