# 此示例示意python的作用域

v = 100  # 全局作用域


def fun1():
    v = 200  # 外部嵌套函数的作用域
    print("fun1内的v=", v)

    def fun2():
        v = 300  # 局部作用域
        print("fun2内的v=", v)
    fun2()


fun1()
print("v=", v)

# 此示例示意global　语句
v = 100


def fn():
    global v
    v = 200


fn()
print(v)

# 此示例示意nonlocal 语句
var = 100


def f1():
    var = 200
    print("f1里的var=", var)

    def f2():
        # global var
        nonlocal var
        var = 300
        print("f2里的var=", var)
    f2()
    print("f2调用结束后f1里的的var值为", var)


f1()
print("全局的var=", var)

# 此示例示意nonlocal 语句嵌套说明


def fx1():
    v = 100

    def fx2():
        v = 200

        def fx3():
            nonlocal v
            v += 1
        fx3()
        print("f2最后的v=", v)
    fx2()
    print("f1最后的v=", v)


fx1()
