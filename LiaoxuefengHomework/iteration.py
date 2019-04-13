# 使用迭代查找一个list中最小和最大值，并返回一个tuple
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return(None, None)
    else:
        MAX = L[0]
        MIN = L[0]
        for x in L:
            if x < MIN:
                MIN = x
            if x > MAX:
                MAX = x
        return(MIN, MAX)
