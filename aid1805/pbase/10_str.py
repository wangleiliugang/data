
#10_str_rectangle.py

#写一个程序，用# 打印一个高度为４的矩形方框
#要求输入一个整数，此整数代表矩形的长度，输出此矩形
#如：请输入长度：10　　　　　打印如下：
#　　　　##########
#    #        #
#    #        #
#　　　　##########

l = int(input("请输入长度："))
line1 = '#' * l
line2 = '#' + ' ' * (l - 2) + '#'
print(line1)
print(line2)
print(line2)
print(line1)


#写一个程序，输入一个字符串，把字符串的第一个字符和最后一个字符去掉，打印出来处理后的字符串

s = input("请输入字符串：")
s2 = s[1:-1]                #s2 = s[1:len(s) - 1]
print('处理后的字符串是：',s2)


#输入任意一个字符串，判断这个字符串是否是回文
#回文是指中心对称的文字．如：上海自来水来自海上　　　　ABCCBA    12321

s = input("请输入字符串：")
a = s[::]
b = s[::-1]
if a == b:
    print(s, "是回文")
else:
    print(s, "不是回文")


#写一个程序，输入一段字符串，如果字符串不为空，则把第一个字符的编码打印出来

s = input("请输入一段字符串：")
if s != '':
    print("第一个字符的编码是：", ord(s[0]))


#写一个程序，输入一个整数值(0-65535),打印出这个数值所对应的字符

n = int(input("请输入一个整数值(0-65535)："))
print("这个数值所对应的字符是：", chr(n))


#用字符串*　运算符打印三角形
#要求输入一个整数，此整数代表此三角形离左侧的字节数
#请输入离左侧的距离：3　　，　则打印如下：
#      *
#     ***
#    *****
#   *******

n = int(input("请输入离左侧的距离："))
print(' ' * (n + 3) + '*')
print(' ' * (n + 2) + '*' * 3)
print(' ' * (n + 1) + '*' * 5)
print(' ' * n + '*' * 7)


#输入三行文字，让这三行文字在一个方框居中显示
#如输入（不要输入中文）：
#hello tarena!
#my name is wangxiaolei
#ptthon3
#  显示如下：
#       hello tarena!
#  my name is wangxiaolei
#         ptthon3

# 方法1
s1 = input("请输入第一行文字：")
s2 = input("请输入第二行文字：")
s3 = input("请输入第三行文字：")
m = max(len(s1), len(s2), len(s3))
n1 = (m - len(s1)) // 2
n2 = (m - len(s2)) // 2
n3 = (m - len(s3)) // 2

print('+' + '-' * m + '+')
print('|' + ' ' * n1 + s1 + ' ' * (m - n1 - len(s1)) + '|')
print('|' + ' ' * n2 + s2 + ' ' * (m - n2 - len(s2)) + '|')
print('|' + ' ' * n3 + s3 + ' ' * (m - n3 - len(s3)) + '|')
print('+' + '-' * m + '+')


# 方法2

s1 = input("请输入第一行文字：")
s2 = input("请输入第二行文字：")
s3 = input("请输入第三行文字：")
m = max(len(s1), len(s2), len(s3))
print('+' + '-' * m + '+')
print('|' + s1.center(m) + '|')
print('|' + s2.center(m) + '|')
print('|' + s3.center(m) + '|')
print('+' + '-' * m + '+')







