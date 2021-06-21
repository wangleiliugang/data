# 此示例示意try-except 语句的用法

def div_apple(n):
    print('%d个苹果您分想给几个人？' % n)
    s = input('请输入人数：')
    cnt = int(s)          # 可能触发ValueError错误异常
    result = n / cnt      # 可能触发ZeroDivisionError错误异常
    print("每个人分了", result,'个苹果')

# 方法1
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('div_apple内出现了ValueError错误，已处理')
    print('用户输入不合法，苹果不分了')
except ZeroDivisionError:
    print('出现被零除的错误！苹果不分了')

print("程序正常退出")

# 方法2
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except (ValueError, ZeroDivisionError):
    print('出现错误！苹果不分了')

print("程序正常退出")

# 此处示意try-except语句中 as 用法
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError as err1:
    print('出现错误！苹果不分了')
    print('错误信息是：', err1)
except ZeroDivisionError as err2:
    print('出现错误！苹果不分了')
    print('错误信息是：', err2)

print("程序正常退出")

# 此处示意try-except中 else 用法
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except:
    print('出现错误，苹果不分了')
else:
    print('程序正常，没有进入过异常状态')

print("程序正常退出")

# 此处示意try-except中 finally 用法
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('值错误，需处理！')
finally:
    print('我是finally 子句，我一定会执行！')

print("程序正常退出")