# -*- coding: utf-8 -*-


import math

# math.floor(3.1)  --> 3   地板除
# math.ceil(3.1)   --> 4


# 使用递归的方法把一个数组中的最大数最小数找出来（建议使用:start+(end-start)/2,代替(start+end)/2-->有溢出风险！）
def maxmin(L, start, end):
    if end - start <= 1:
        return (max(L[start], L[end]), min(L[start], L[end]))
    else:
        max1, min1 = maxmin(L, start, math.floor((start + end) / 2))
        max2, min2 = maxmin(L, math.floor((start + end) / 2) + 1, end)
        return (max(max1, max2), min(min1, min2))


L = [1, 5, -9, 7, -1, 12, 3, 8]
maxV, minV = maxmin(L, 0, len(L) - 1)
print(maxV, minV)
