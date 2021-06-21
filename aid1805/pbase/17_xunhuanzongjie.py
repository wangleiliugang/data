# 输入一个整数n　，判断这个整数是否是素数(prime),(素数是指只能被1　和自身整除的数)
# 如2　3　5　7　11　．．．
# 用排除法：一但n能被2～n-1的数整除，那么这个数就不是素数，否则就一定是素数


# 方法1
n = int(input("请输入一个整数："))

if n < 2:
    print(n, "不是素数！")
    exit()

flag = True   # True 代表是素数，False 代表不是素数
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
if flag == True:
    print("这个数是素数！")
else:
    print("这个数不是素数！")

# 方法２

s = int(input("请输入一个整数："))
for x in range(2, s):
    if s % x == 0:
        print(s, "不是素数：","可以被整除的数是：", x)
        break
else:
    print(s, "是素数！")


# 1.输入一个整数，代表树干的高度，打印一颗"圣诞树"
# 如输入：２　　　　　　　　　　　如输入：3
#　　　　　　　　*　　　　　　　　　　　　　　　　　　*
#　　　　　　　***　　　　　　　　　　　　　　　　***
#　　　　　　　　*　　　　　　　　　　　　　　　　*****
#　　　　　　　　*　　　　　　　　　　　　　　　　　　*　
#　　　　　　　　　　　　　　　　　　　　　　　　　　　*
#                       　　　　*

n = int(input("请输入圣诞树的树干高度："))
i = 1

while i <= n:
    w = 2 * i - 1
    print(' ' * (n - i) + '*' * w + ' ' * (n - i))
    i += 1
while True:
    print(' ' * (n - 1) + '*' +' ' * (n - 1))
    i += -1   # 注意：此时i = 4 - 1
    if i <= 1:
        break
# 方法2
for x in range(1, n+1):
    print(' ' * (n - x) + '*' * (2 * x - 1) + ' ' * (n - x))
for x in range(1, n+1):
    print(' ' * (n - 1) + '*')


# 2.用循环语句生成如下字符串
# 'ABC......XYZ'
# 'AaBbCc......XxYyZz'
# 提示：用ord 和　chr 函数结合循环语句实现

for x in range(65, 91):
    print(chr(x), end='')
print()

for x in range(65, 91):
    print(chr(x),end='')
    print(chr(x + 32), end='')
print()

# 方法2
s = ''
s2 = ''
for i in range(65, 65+26):
    s += chr(i)
    s2 += chr(i)
    s2 += chr(i + 32)
    # ord('a') - ord('A') = 32
print(s)
print(s2)


#　算出100～999以内的水仙花数(Narcissistic number)
# 水仙花数是指百位的3次方加上十位的3次方加上个位的3次方等于原来的数字
#　例如：153 = 1**3 + 5**3 + 3**3
# 参考答案：153，　370，．．．

# 方法1
for n in range(100,1000):
    a = n // 100
    b = n // 10 % 10
    c = n %10
    if a ** 3 + b ** 3 + c ** 3 == n:
        print(n, "是水仙花数！")
# 方法2
for x in range(100,1000):
    s = str(x)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if x == a ** 3 + b ** 3 + c ** 3:
        print(x, "是水仙花数！")

# 方法3
for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            i = (x * 100 + y * 10 + z)
            if (x ** 3 + y ** 3 + z ** 3) == i:
                print(i, '是水仙花数！')



































