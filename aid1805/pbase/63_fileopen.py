# 此示例示意　文件的打开和关闭，及错误处理

try:
    # f = open('/etc/passwd')  # 文件存在，可以成功打开
    f = open('/root/abc.txt')  # 文件不存在

    print("文件打开成功！")

    # 在此处进行文件的读写操作

    f.close()
except OSError:
    print("打开文件失败！")
