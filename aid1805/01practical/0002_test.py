
# def cal_func(func):
#     num = 0

#     def cal_counter(*args, **kwargs):
#         nonlocal num
#         num += 1
#         func(*args, **kwargs)
#         print('我被调用了', num, '次')
#     return cal_counter


# @cal_func
# def test():
#     pass


# test()
# test()
# test()

# 第1题
def write_to_file(dic, filename='./cache'):
    try:
        f = open(filename, 'w')
        for i in dic:
            f.write(str(dic))
        f.close()
    except OSError:
        raise OSError("文件打开失败！")

class cal_counter(object):

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@cal_counter
def func1():
    dic = {"times": func1.count}
    write_to_file(dic)


func1()
func1()
func1()


# 第2题
def func(list1, list2):
    a = [x for x in list1 if x in list2]
    b = [y for y in (list1 + list2) if y not in a]
    return a, b


print(func([1, 3, 6, 23, 8], [3, 5, 8, 10]))


# 第4题
import time
import datetime


now = datetime.datetime.now()
# 函数接收时间元组，返回自定义格式"%Y%m%d"的时间字符串
t = now.strftime("%Y%m%d")
date_time = t[:4] + '年' + t[4:6] + '月' + t[6:] + '日'


def cal_time(date1, date2=date_time):
    # 根据指定的格式把一个时间字符串解析为时间元组对象
    date1 = time.strptime(date1, "%Y年%m月%d日")
    date2 = time.strptime(date2, "%Y年%m月%d日")

    # 返回一个date类型的对象
    date1 = datetime.date(date1[0], date1[1], date1[2])
    date2 = datetime.date(date2[0], date2[1], date2[2])
    return print("日期差为:", abs((date2 - date1).days), '天')


cal_time("2021年06月01日", "2021年01月01日")
cal_time("2021年01月01日")


# 面试题1
# 编程实现，将字符串a变成b
a = 'i   am   RPA'
b = 'RPA am i'

l1 = []
s = a.split(" ")
for i in s:
    if i == '':
        continue
    l1.append(i)
l1 = l1[::-1]
l2 = ' '.join(l1)
print(l2)


# 面试题2
# 将二维数组a1降维编程b1
a1 = [[1, 2], [2, 3], [3, 4]]
b1 = [1, 2, 2, 3, 3, 4]

# a2 = a1[0] + a1[1]
# print(a2)
lst = []
for i in a1:
    lst += i
print(lst)


# 面试题3
# 不可变数据类型：
# 　　int, float, complex, bool, str, tuple, frozenset, bytes(字节串)
# 可变数据类型：
#   list, dict, set, bytearray(字节数组)
