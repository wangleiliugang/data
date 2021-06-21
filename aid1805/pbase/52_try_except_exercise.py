#　写一个函数get_score() 来获取学生的成绩(0-100),如果输入出现异常，则此函数返回0,否则返回用户输入的成绩

# 方法1
def get_score():
    try:
        score = float(input("请输入学生成绩："))
    except:
        return 0

    if 0 <= score <= 100:
        return score
    return 0

score = get_score()
print("学生的成绩是：", score)


# 方法2
def get_score():
    score = float(input("请输入学生成绩："))
    if 0 <= score <= 100:
        return score
    else:
        return 0
try:
    score = get_score()
except:
    score = 0
print("学生的成绩是：", score)