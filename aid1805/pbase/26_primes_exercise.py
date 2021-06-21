# 素数prime 函数练习
# 1.写一个函数isprime(x) 判断x 是否为素数，如果是素数，返回True,否则返回False
# 方法1
def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(isprime(2))
print(isprime(9))

# 2.写一个函数prime_m2n(m, n),返回从m到n结束(不包含n)的范围内的素数列表：
# 如：L = prime_m2n(1, 10)         print(L)     # [2,3,5,7]

# 方法1
def prime_m2n(m, n):
    L = []
    i = m                   # for i in range(m, n):
    while i < n:            #     if isprime(i):
        if isprime(i):      #         L.append(i)
            L.append(i)     # return L
        i += 1
    return L

L = prime_m2n(1, 12)
print(L)

# 方法2
def prime_m2n(m, n):
    return [x for x in range(m, n) if isprime(x)]  # 用列表推导式可以实现

L = prime_m2n(1, 12)
print(L)

# 3.写一个函数primes(n),返回指定范围内素数(不包含n)的全部素数的列表，并打印这些素数
# 如：L = primes(20)              print(L)      # [2,3,5,7,11,13,17,19]
# 1)打印100以内的全部素数
# 1)打印100以内的全部素数的和

def primes(n):
    return prime_m2n(0, n)

L = primes(20)
print(L)
print('100以内的全部素数有：',primes(100))
print('100以内的全部素数的和是：',sum(primes(100)))