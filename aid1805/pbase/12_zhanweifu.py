# 输入三行文字，让这些文字依次以20 字符的宽度右对齐输出
# 示例：请输入第1行：hello world
#     请输入第2行：abcd
#     请输入第3行：a
# 输出结果：
#            hello world
#                   abcd
#                      a

s1 = input('请输入第1行：')
s2 = input('请输入第2行：')
s3 = input('请输入第3行：')
print("%20s" % s1)
print('%20s' % s2)
print("%20s" % s3)


# 以下按最长的字符串右对齐
# 方法1
m = max(len(s1), len(s2), len(s3))
print("最大长度是：", m)
print(' ' * (m - len(s1)) + s1)
print(' ' * (m - len(s2)) + s2)
print(' ' * (m - len(s3)) + s3)

# 方法2
f = '%%%ds' % m     # 生成一个含有占位符的字符串
print('f =', f)
print(f % s1)
print(f % s2)
print(f % s3)
