# 1.求　1 ** 2 + 2 ** 2 + 3 ** 2 + ... + 9 ** 2 的和


# 方法1
def mypow(x):
    return x ** 2


print(sum(map(mypow, range(1, 10))))
# 方法2
print(sum(map(lambda x: x ** 2, range(1, 10))))
# 方法3
print(sum(map(pow, range(1, 10), [2, 2, 2, 2, 2, 2, 2, 2, 2])))  # 使用内建pow函数


# 2.求　1 ** 3 + 2 ** 3 + 3 ** 3 + ... + 9 ** 3 的和
def mypow(x):
    return x ** 3


print(sum(map(mypow, range(1, 10))))

# 3.求　1 ** 9 + 2 ** 8 + 3 ** 7 + ... + 9 ** 1 的和    # 11377
# 方法1
s = 0
for x in map(pow, range(1, 10), range(9, 0, -1)):
    s += x
print(s)
# 方法2
print(sum(map(pow, range(1, 10), range(9, 0, -1))))
# 方法3
print(sum(map(lambda x, y: x ** y, range(1, 10), range(9, 0, -1))))
