# 输入一个字符串
# 1．判断您输入的字符串有几个空格
# 2．将原字符串的左右空白字符去掉，打印出有效字符的长度
# 3．判断您输入的是否是数字


s = input('请输入一个字符串：')
print('您输入的字符串有：', s.count(' '), '个空格')

s2 = s.strip()
print('有效字符的长度是：', len(s2))

if s2.isdigit():
    print('您输入的是数字')
else:
    print('您输入的不是数字')


# 示意字符串格式化表达式的用法

fmt = "姓名：＿%s＿, 年龄：＿%d＿"
name = input("请输入姓名：")
age = int(input("请输入年龄："))
s = fmt % (name, age)
print(s)
