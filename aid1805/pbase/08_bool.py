# 08_bool.py


score = input("请输入成绩:") or '0'
score = int(score)
if score < 0 or score > 100:
    print("您输入的成绩不合法！")
else:
    print("您输入的成绩是：", score)
