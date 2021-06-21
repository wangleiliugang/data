# 此示例示意用raise 语句发出错误通知给调用者

# 甲写了函数 get_age
def get_age():
    a = int(input("请输入年龄(0~150):"))
    if 0 <= a <= 150:
        return a
    if a > 150 or a < 0:
        raise OverflowError("人的年龄不可能大于150岁或者小于0岁!!!")


# 乙用户调用get_age
try:
    age = get_age()
except ValueError as err:
    print("用户输入的不是数字类型，已做相应处理！")
    age = 0
except OverflowError as err:
    print("错误信息是：", err)
    age = 0

print("得到的年龄是：", age)
