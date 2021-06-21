# 此示例示意函数装饰器用法
def mydeco(fn):
    def fx():
        print("++++++++++")
        fn()
        print("----------")
    return fx

@mydeco      # 等同于myfunc = mydeco(myfunc)   
def myfunc():
    print("myfunc被调用")

myfunc()
myfunc()
myfunc()

# 此示例示意带有参数的装饰器及应用案例
# 银行业务：存钱　savemoney
#          取钱　withdraw 
# 1.添加一个余额变动提醒短消息功能
def message_send(fn):
    def fx(name, x):
        print("发送消息：", name, "来银行办理业务...")
        fn(name, x)
        print("发送消息：", name, "办理了", x, "元的业务...")
    return fx
# 2.增加一个权限验证功能的装饰器
def privileged_check(fn):
    def fx(name, x):
        print("正在验证权限...")
        if True:
            fn(name, x)
    return fx

@privileged_check
@message_send
def savemoney(name, x):
    print(name, "存钱", x, "元")

@message_send
def withdraw(name, x):
    print(name, "取钱", x, "元")

# 以下是调用者小张定的程序
savemoney("小李", 200)
savemoney("小赵", 500)
withdraw("小王", 300)

