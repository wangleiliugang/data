# 此示例以建房子为例说明在什么情况下使用异常处理机制

# 示例１
def f1():
    print('开始给房子打地基')

    return ValueError("地下发现文物！")
    print('...')
    print('地基已完成!')
    return 0


def f2():
    print('开始建地面以上部分')
    return ValueError("地上要修高压线！")
    print('...')
    print('高楼建完!')
    return 0


def f3():
    r = f1()
    if r != 0:
        return r
    r1 = f2()
    if r1 != 0:
        return r1


def built_house():
    r = f3()
    if r != 0:
        return r


r = built_house()
if r == 0:
    print("房子已建完")
else:
    print("房子没建完", r)


# 示例２
def f11():
    print('开始给房子打地基')
    raise ValueError("地下发现文物！")
    print('...')
    print('地基已完成!')
    return 0


def f22():
    print('开始建地面以上部分')
    raise ValueError("地上要修高压线！")
    print('...')
    print('高楼建完!')
    return 0


def f33():
    f11()
    f22()


def built_house():
    f33()


try:
    built_house()
except ValueError as err:
    print("房子没有建完", err)
else:
    print("房子建完了!")
