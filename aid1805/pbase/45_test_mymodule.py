# 此程序用于示意模块mymodule，并调用相应的数据和函数

import mymodule1
from mymodule1 import name2
from mymodule1 import *


mymodule1.myfun1()
print(mymodule1.name1)
print("mymodule里的name2为：", name2)

myfun2()
