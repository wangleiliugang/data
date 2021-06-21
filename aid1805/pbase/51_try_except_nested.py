# 此示例示意try-except 语句的嵌套用法

# 示例1
def div_apple(n):
    print('%d个苹果您分想给几个人？' % n)
    s = input('请输入人数：')
    cnt = int(s)          # 可能触发ValueError错误异常
    try:
        result = n / cnt      # 可能触发ZeroDivisionError错误异常
        print("每个人分了", result,'个苹果')
    except ZeroDivisionError:
        print('被零除错误！')

try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('div_apple内出现了ValueError错误，已处理')
else:
    print('此try 语句没有进入异常状态')
finally:
    print('我是finally 子句，我一定会执行')
print("程序正常退出！")

# 示例2
def div_apple(n):
    print('%d个苹果您分想给几个人？' % n)
    s = input('请输入人数：')
    try:
        cnt = int(s)          # 可能触发ValueError错误异常
        result = n / cnt      # 可能触发ZeroDivisionError错误异常
        print("每个人分了", result,'个苹果')
    except ZeroDivisionError:
        print('被零除错误！')

try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('div_apple内出现了ValueError错误，已处理')
else:
    print('此try 语句没有进入异常状态')
finally:
    print('我是finally 子句，我一定会执行')
print("程序正常退出")