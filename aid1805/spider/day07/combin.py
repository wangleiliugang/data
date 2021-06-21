# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:10:05 2020

@author: 13775
"""

#n >= m，C(n,m) = n!/(m!(n-m)!) = C(n,n-m)  = C(n-1,m-1) + C(n-1,m)

def ComNum(n,m):
    """
    使用递归方法来计算C(n,m) = n!/(m!(n-m)!)
    """
    if m==0 or m==n:
        return 1 
    return ComNum(n-1,m-1)+ComNum(n-1,m)

n,m = 5,3
print(ComNum(n,m))


#如何解决递归中重复运算带来的空间和时间上的浪费？
#怎么将已经算出的方法保存下来，并且方便查询出计算结果？
#这里可以使用DP（动态规划）。
#思路：使用二维数组numpy存储已经计算过的数值，后续重复的计算不在需要计算而是从已经存储的数组中直接查找。-->空间换时间的思想。
