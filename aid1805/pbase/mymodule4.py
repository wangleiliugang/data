
'''这是模块的文档字符串的标题

这是文档字符串的内容
此模块包含两个函数和两个变量
'''

def f1():
    '''这是函数f1的文档字符串'''
    pass
def f2():
    '''这是函数f2的文档字符串'''

    pass
name1 = 'audi'
name2 = 'BMW'
# print(__doc__)


# 此处示意__name__列表的作用和用法
def f3():
    print("f3被调用")

if __name__ == '__main__':
    print("mymodule4.py 正在当做主模块运行")
    f3()
else:
    print("mymodule4.py 正在被其它模块导入")
    print("模块名为：", __name__)


# 此处示意__all__列表的作用和用法
# 限制用from mymodule4 import * 时只导入f4, var1
__all__ = ['f4', 'var1']

def f4():
    pass
def f5():
    pass
var1 = 'hello'
var2 = 'world'


