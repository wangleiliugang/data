# 1.用生成器函数primes(begin, stop)生成素数，给出起始值begin和终止值stop，生成此范围内的全部素数，不包含(stop)
# 如：L = [x for x in primes(10, 20)]　　　　　得到列表L = [11, 13, 17, 19]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def myprimes(begin, stop):
    for x in range(begin, stop):
        if is_prime(x):
            yield(x)

# def myprimes(begin, stop):
#     i = begin
#     while i < stop:
#         if is_prime(i):
#             yield i
#         i += 1

L = [x for x in myprimes(10, 20)]
print(L)

# 仿制range函数的功能，写一个生成器函数myrange，要求功能与range功能相近，能实现一个，两个，三个参数传参，生成正向的整数
# 如：for x in myrange(1, 10, 3):
#        print(x)      得到：1, 4, 7
def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    i = start
    while i < stop:
        yield i
        i += step

print(list(myrange(5)))
print(list(myrange(10, 15)))
for x in myrange(1, 10, 3):
    print(x)
