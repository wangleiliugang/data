# 此示例示意模块的导入语句　import语句
# 1.输入一个正方形的周长，输出正方形的面积
# 2.输入一个圆的半径，打印出这个圆的面积
# 3.输入一个正方形的面积，打印这个正方形的周长
# (要求：用math 模块内的函数和数据)

# 导入math 模块
import math    # import math as m (或者from math import pi,pow,sqrt)
               #　使用m.函数名调用       此处直接使用模块内的函数名调用即可
p = float(input("请输入正方形周长:"))
area = math.pow(p / 4, 2)
print("正方形的面积是：", area)

r = float(input("请输入圆的半径:"))
area = math.pi *math.pow(r, 2)
print("圆的面积是：", area)

s = float(input("请输入正方形的面积:"))
p = math.sqrt(s) * 4
print("正方形的周长是是：", p)

