# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:01:51 2020

@author: 13775
"""
#输入正整数n，如果n=4，输出如下结果：
#    10 11 12 1
#    9  16 13 2
#    8  15 14 3
#    7  6  5  4

import numpy as np


def PrintSnakeMatrix(n):
    myArray = np.zeros((n, n), dtype=np.int16)
    num = 1
    i = 0     #记录行标
    j = n-1   #记录列标
    myArray[i][j] = num
    
    while num < n*n:
        while (i+1 < n and myArray[i+1][j] == 0):#向下；行标不断增大，列标不变。
            i += 1
            num += 1
            myArray[i][j] = num
        while (j-1 >= 0 and myArray[i][j-1] == 0):#向左；行标不变，列标减小。
            j -= 1
            num += 1
            myArray[i][j] = num
        while (i-1 >= 0 and myArray[i-1][j] == 0):#向上
            i -= 1
            num += 1
            myArray[i][j] = num
        while (j+1 < n and myArray[i][j+1] == 0):#向右
            j += 1
            num += 1
            myArray[i][j] = num
    print(myArray)


n = int(input("请输入正整数n的值："))
PrintSnakeMatrix(n)
