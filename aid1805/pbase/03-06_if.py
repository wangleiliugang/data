# if.py
# 输入一个数，让计算机判断是奇数还是偶数

s = input("请输入一个数：")
n = int(s)
if n % 2 == 1:
    print("您输入的是奇数")
else:
    print("您输入的是偶数")


# 任意输入一个数判断是否大于100，是否在20～50之间

n = int(input("任意输入一个数："))
if n > 100:
    print(n, "大于100")
else:
    print(n, "不大于100")

if 20 < n < 50:
    print(n, "在20～50之间")
else:
    print(n, "不在20～50之间")


# if-elif-else 示例
# 输入一个数，判断这个数是正数，负数还是0

n = int(input("请输入任意一个数："))
if n == 0:
    print("您输入的是0")
elif n > 0:
    print(n, "是正数")
else:
    print(n, "是负数")


# 输入一个季度1～4，输出这个季度有哪几个月，如果输入的不是1～4的数，提示用户＂您的输入有误！＂

season = int(input("请输入一个季度（1～4）："))
if season == 1:
    print("春季有：1月，2月，3月")
elif season == 2:
    print("夏季有：4月，5月，6月")
elif season == 3:
    print("秋季有：7月，8月，9月")
elif season == 4:
    print("冬季有：10月，11月，12月")
else:
    print("您的输入有误！")

# 输入一年中的月份（1～12），判断在哪个季节，如果输入不是1～12月份，提示用户＂您的输入有误！＂

month = int(input("请输入月份："))
if 1 <= month <= 3:
    print("春季")
elif 4 <= month <= 6:
    print("夏季")
elif 7 <= month <= 9:
    print("秋季")
elif 10 <= month <= 12:
    print("冬季")
else:
    print("您的输入有误！")

month = int(input("请输入月份："))
if 1 <= month <= 12:
    print("是合法月份")
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您的输入有误！")


# 输入一个同学的成绩（0-100）;
# 判断该同学的成绩是优（90-100），良（80-89），及格（60-79），不及格（0-59）及输入成绩不合法5中状态.

score = int(input("请输入成绩："))
if 0 <= score <= 100:
    print("成绩合法")  # 该条语句可以去掉
    if score < 60:
        print("不及格")
    elif score < 80:
        print("及格")
    elif score < 90:
        print("良")
    else:
        print("优")
else:
    print("您输入的成绩不合法！")


# 条件表达式的用法
# 商场促销，满100返20

money = int(input("请输入商品总额："))
pay = money - 20 if money >= 100 else money
print("您需要支付：", pay, "元")


# 输入一个数
# 1.用if 语句计算出这个数的绝对值并打印出来
# 2.用条件表达式计算出这个数的绝对值并打印出来

n = int(input("请输入一个数："))
# 方法1
if n < 0:
    absolue = -n
else:
    absolue = n
print("if语句计算的绝对值是：", absolue)

# 方法2
absolue = n
if absolue < 0:
    absolue = -absolue
print("if语句计算的绝对值是：", absolue)

# 方法3
absolue = -n if n < 0 else n
print("if语句计算的绝对值是：", absolue)
