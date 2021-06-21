# 09_exercise.py

# 1.北京出租车计费
#  收费标准：3公里以内收费13元;超过3公里后基本单价为2.3元/公里
#         　空驶费：超过15公里后，每公里加收基本单价的50％作为返程的空驶费（3.45元/公里）
#  要求：输入公里数，打印出费用的金额（以元为单位进行四舍五入）

kilometre = int(input("请输入行使公里数："))
base1 = 13
base2 = base1 + 2.3 * (kilometre - 3)
base3 = base2 + 1.15 * (kilometre - 15)
if kilometre <= 3:
    print("您的消费金额是：", base1, "元")
elif kilometre <= 15:
    print("您的消费金额是：", round(base2), "元")
else:
    print("您的消费金额是：", round(base3), "元")

# 方法2
# fee = 13
# if km > 3:
#    fee += 2.3 * (km - 3)
# if km > 15:
#    fee += 1.15 * (km - 15)
# print('消费金额是：', round(fee), '元')


# ２.输入一个同学的三科成绩：打印出最高成绩／打印出最低成绩／打印出平均成绩

score1 = int(input("请输入第一科成绩："))
score2 = int(input("请输入第二科成绩："))
score3 = int(input("请输入第三科成绩："))
if score1 >= score2 >= score3 or score1 >= score3 >= score2:
    print("最高成绩是：", score1)
elif score2 >= score1 >= score3 or score2 >= score3 >= score1:
    print("最高成绩是：", score2)
else:
    print("最高成绩是：", score3)
if score1 <= score2 <= score3 or score1 <= score3 <= score2:
    print("最低成绩是：", score1)
elif score2 <= score1 <= score3 or score2 <= score3 <= score1:
    print("最低成绩是：", score2)
else:
    print("最低成绩是：", score3)
print("平均成绩是：", (score1 + score2 + score3) / 3)

# 经典算法：
# m = s1
# if s2 >= m:
#    m = s2
# if s3 >= m:
#    m = s3
# print("最高成绩是：", m)


# 3.给出一个年份，判断是否为闰年并打印结果
#  润年规则：每四年一闰，每百年不闰，四百年又是一个闰年．　　例：2016年　润年／2100年　不是润年／2400年　润年

years = int(input("请输入年份："))
if years % 400 == 0:
    print(years, "年是闰年")
elif years % 100 != 0 and years % 4 == 0:
    print(years, "年是闰年")
else:
    print(years, "年不是闰年")


# 4.BMI　指数（Body Mass Index） 也称身体质量指数
#  BMI值计算公式：BMI = 体重（公斤） / 身高（米）的平方
#  例如：一个69公斤的人，身高是173公分
#      BMI = 69 / 1.73 ** 2 = 23.05
#  标准表：BMI < 18.5            (体重过轻)
#        18.5 <= BMI <= 24     (正常范围)
#        BMI > 24              (体重过重)
# 请输入身高和体重，打印BMI 值，并打印体重状况

weigth = int(input("请输入体重(公斤)："))
heigth = float(input("请输入身高(米)："))
a = weigth / heigth ** 2
print("您的BMI值是：", a)
if a < 18.5:
    print("您的体重过轻")
elif 18.5 <= a <= 24:
    print("您的体重正常")
else:
    print("您的体重超标")
