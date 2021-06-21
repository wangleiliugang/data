# 此示例示意用try-except 和　try-finally语句组合来对文件进行操作
def read_from_file(filename='info.txt'):
    try:
        f = open(filename)
        try:
            print("正在读取文件...")
            n = int(f.read())
            print("n=", n)
        except:
            f.close()
            print("文件已经关闭!")
    except OSError:
        print("文件打开失败!")

read_from_file()


# 用with 语句可以实现同样的功能
def read_from_file(filename='info.txt'):
    try:
        with open(filename) as f:
            print("正在读取文件...")
            n = int(f.read())
            print("n=", n)
            print("文件已经关闭!")
    except OSError:
        print("文件打开失败!")

read_from_file()