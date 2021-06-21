import numpy as np


# 可以先把list重新排序，然后从list的最后开始扫描，代码如下：
def distFunc3():
    List = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    if List:
        List.sort()
        print(List)
        last = List[-1]
        print(last)
        for i in range(len(List) - 2, -1, -1):
            if last == List[i]:
                del List[i]
            else:
                last = List[i]
    print(List)


if __name__ == '__main__':
    distFunc3()

l1 = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
a = np.unique(l1)
print(a)
print(type(a))
print(list(a))
