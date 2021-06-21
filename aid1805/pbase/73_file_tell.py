# 此示例示意用f.tell()方法获取文件当前的读写位置
try:
    f = open('data.txt', 'rb')
    print("当前的读写位置是：", f.tell())
    b = f.read(5)
    print("当前的读写位置是：", f.tell())
    b = f.read()
    print("文件最后的位置是：", f.tell())
    f.close()
except OSError:
    print('打开文件失败！')