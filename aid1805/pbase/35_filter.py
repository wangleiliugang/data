# 1.将1-20　内的偶数用filter　筛选出来，形成列表
# 方法1
print([x for x in filter(lambda x: x % 2 == 0, range(1, 20))])
# 方法1
L = list(filter(lambda x: x % 2 == 0, range(1, 20)))
print(L)

# 2.用filter 函数将1-100之间的所有素数(prime)放入到列表中
def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
L = list(filter(isprime, range(1, 100)))
print(L)

