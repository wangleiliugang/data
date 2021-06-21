# 此示例示意assert 语句的用法

def get_age():
    a = int(input("请输入年龄："))
    assert 0 <= a <= 150, "年龄不在合理范围内!!!"
    return a


try:
    age = get_age()
except AssertionError as e:
    print("错误信息是：", e)
    age = 0

print("年龄是：", age)
