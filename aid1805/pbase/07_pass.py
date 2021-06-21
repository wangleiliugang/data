# 07_pass.py

# 判断一个学生的成绩是否合法．如果不合法给出警告信息;如果合法什么都不做

score = int(input("请输入成绩："))
if 0 <= score <= 100:
    pass
else:
    print("您的输入有误！")
print("程序结束")
