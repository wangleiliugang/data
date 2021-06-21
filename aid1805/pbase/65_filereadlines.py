# 此示例示意f.readlines的用法

try:
    f = open("info.txt")
    L = f.readlines()
    print(L)
    f.close()
except OSError:
    print("打开info.txt文件失败！")