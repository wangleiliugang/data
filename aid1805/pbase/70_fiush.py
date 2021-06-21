import time

# 1.0
f = open('infos.txt', 'w')
f.write('hello world!')
print("程序开始睡觉...zzz")
time.sleep(15)
print("程序睡醒了，继续执行！")

f.close()


# 2.0
f = open('infos.txt', 'w')
f.write('hello world!')

for i in range(10000):
    f.write('hello world!')
    time.sleep(0.01)

f.close()


# 3.0
f = open('infos.txt', 'w')
f.write('hello world!')
f.flush()  # 强制清空缓冲区
print("程序开始睡觉...zzz")
time.sleep(15)
print("程序睡醒了，继续执行！")

f.close()