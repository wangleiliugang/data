a = 100
b = 200
def fx(c):
    d = 400
    print(a, b, c, d)

fx(300)
print('a =', a)
print('b =', b)
# print('c =', c)  出错，局部变量无法访问
# print('d =', d)　　出错，局部变量无法访问

a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    print("locals()返回", locals())
    print("globals()返回", globals())
    for k, v in globals().items():
        print(k,'******', v)
    print(c)                 # 100
    print(globals()['c'])    # 得到全局变量c 的值3

fn(100, 200)


