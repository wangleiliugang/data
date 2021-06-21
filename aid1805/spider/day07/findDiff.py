# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:32:15 2020

@author: 13775
"""

#def FindDiff(L1, L2):
#    """
#    找出L1，L2中丢失的那1个元素
#    """
#    if len(L1) > len(L2):
#        for i in L1:
#            if i not in L2:
#                return i
#    else:
#        for j in L2:
#            if j not in L1:
#                return j
            
def FindDiff2(L1, L2):
    s1 = sum(L1)
    s2 = sum(L2)
    if s1 > s2:
        return s1 - s2
    else:
        return s2 - s1

#L1 = [1,3,5,7,2,4,6,8]
#L2 = [1,5,7,4,2,8,6]
#assert(FindDiff(L1,L2) == 3)
#L1 = [1,3,5,7,2,4,6,8]
#L2 = [1,5,3,7,4,2,8,10,6]
#assert(FindDiff(L1,L2) == 10)


L1 = [1,3,5,7,2,4,6,8]
L2 = [1,5,7,4,2,8,6]
assert(FindDiff2(L1,L2) == 3)
L1 = [1,3,5,7,2,4,6,8]
L2 = [1,5,3,7,4,2,8,10,6]
assert(FindDiff2(L1,L2) == 10)
