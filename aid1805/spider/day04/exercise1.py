# 如何从一个list中去除重复的元素，至少使用2钟方法实现。


def DelDuplist(L):
    # return list(set(L))
    lst = sorted(set(L), key=L.index)
    return lst


# 使用字典中key值的唯一性解决
def DelDuplist1(L):
    myDict = {}
    for i in L:
        myDict[i] = 0
    L = list(myDict.keys())
    return L


def DelDuplist2(L):
    lst = []  # 空间复杂度会增加
    for l1 in L:
        if l1 not in lst:
            lst.append(l1)
    return lst


def DelDuplist3(L):
    for i in L:
        while L.count(i) > 1:  # list中元素移除之后，下标会改变，所以需要使用while。
            L.remove(i)
    return L


L = [1, 3, 3, 3, 4, 3, 34, 3, 54, 3, 4, 2, 8]
print('方法0:', DelDuplist(L))  # [1,3,4,34,54,2,8]
print('方法1:', DelDuplist1(L))
print('方法2:', DelDuplist2(L))
print('方法3:', DelDuplist3(L))


# 不会增加空间复杂度
def distFunc3(List):
    # 可以先把list重新排序，然后从list的最后开始扫描，代码如下：
    if List:
        List.sort()
        last = List[-1]
        for i in range(len(List) - 2, -1, -1):
            if last == List[i]:
                del List[i]
            else:
                last = List[i]
    return List


List = [1, 3, 3, 3, 4, 3, 34, 3, 54, 3, 4, 2, 8]
print(distFunc3(List))
