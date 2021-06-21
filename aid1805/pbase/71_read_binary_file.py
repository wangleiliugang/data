# 此示例示意以二进制方式读取文件内容
# try:
#     f = open('infos.txt', 'rb')
#     # 读取数据，常用f.read读取
#     b = f.read(5)    # 5  代表5个字节(bytes)
#     print(b)
#     b = f.read(2)
#     print(b)
#     b = f.read()     # 不加实参读取全部字节，直至文件尾
#     print(b)

#     f.close()
# except OSError:
#     print("打开文件失败！")


# 此示例示意以二进制方式读取文件内容，然后再将其转换为字符串
try:
    f = open('infos.txt', 'rb')
    # 读取数据，常用f.read读取
    b = f.read(5)    # 5  代表5个字节(bytes)
    print(b)
    b += f.read(2)
    print(b)
    b += f.read()     # 不加实参读取全部字节，直至文件尾
    print(b)
    print('读取的内容转为文字后为：', b.decode('utf-8'))

    f.close()
except OSError:
    print("打开文件失败！")