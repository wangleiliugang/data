# -*- coding: utf-8 -*-


# 使用递归计算斐波那契数
def Fab(n):
    # 0 <= n并且n是正整数
    if type(n) != type(1) or n < 0:
        print("非法输入！")
        return None
    if n < 2:
        return 1
    else:
        return Fab(n - 1) + Fab(n - 2)


for i in range(0, 10):
    print(Fab(i))
