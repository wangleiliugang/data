# 1.一个皮球从100米高空落下，每次落下后反弹高度是原来高度的一半，然后再落下
# 算出皮球在第10次落地后反弹高度是多少？
# 打印出皮球共经历了多少米的路程
def ball_highly(height, times):
    for _ in range(times):
        height /= 2
    return height


def ball_distance(height, times):
    s = 0
    for _ in range(times):
        s += height  # 把下落高度累加到S中
        height /= 2
        s += height  # 把反弹高度累加到S中
    return s
print('皮球从100米高空落下反弹10次后高度是：', ball_highly(100, 10), '米')
print('皮球反弹10次后共经历了：', ball_distance(100, 10), '米')


# 2.输入一个正整数，分解质因数.
# 如输入：90     打印：90=2*3*3*5
# 质因数是指最小能被原数整除的素数(不包括1)
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def get_prime_list(n):
    L = []
    while not is_prime(n):
        for i in range(2, n):
            if is_prime(i) and n % i == 0:
                L.append(i)
                n /= i  # 除以因数后，n的值为float类型
                n = int(n)
                break
    else:
        L.append(n)
    return '*'.join(map(str, L))


if __name__ == '__main__':
    n = int(input("请输入整数："))
    print(n, '=', get_prime_list(n))
