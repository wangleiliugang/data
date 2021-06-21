# 已知有序列　L = [3, 5]
# 用索引和切片操作，将列表改为：L = [1, 2, 3, 4, 5, 6]
# 将列表反转(前后对调)，然后删除最后一个元素　print(L)    # [6, 5, 4, 3, 2]

L = [3, 5]
L[0:2] = [1, 2, 3, 4, 5, 6]
X = L[::-1]      # L[:] = L[::-1]
del X[5]         # del L[-1]
print(X)


# 写程序，让用户循环输入一些整数，当输入-1 时结束输入，将这些整数存于列表L 中
# 1.打印您一共输入了几个有效的数？
# 2.打印您输入的数的最大数是多少？
# 3.打印您输入的数的最小数是多少？
# 4.打印您输入这些数的平均值是多少？


L = []
while True:
    n = int(input("请输入整数(输入-1程序结束！)："))
    if n == -1:
        break
    L[0:0] = [n]       # L += [n]
X = L[::-1]

print(X)
print("有效数字个数是：", len(L))
print("最大数是：", max(L))
print("最小数是：", min(L))
print("平均值是：", sum(L) / len(L))


# 写一个程序，输入多行文字，当输入空行时结束输入，将原输入的所有字符串存于列表Ｌ中
# 1.按原来输入的行的顺序反向打印这些行
# 示例：输入：hello world
#      输入：welcome to china
#      输入：I like python
#      输入：<回车键>

# 显示：I like python
#      welcome to china
#      hello world

L = []
while True:
    w = input("请输入一行文字：")
    if w == '':                 # if not w:w为空则跳出循环
        break
    L[0:0] = [w]                # L.append(w)追加到Ｌ中
for x in L:
    print(x)

# 2.打印出您一共输入了多少个文字符？

s = 0
for x in L:
    s += len(x)
print("您一共输入的字符个数是：", s)


# 用列表推导式生成1~100内的奇数的列表，结果[1, 2, 3, ...99]
L = [x for x in range(1, 100, 2)]   # L = [x for x in range(1, 100) if x % 2 == 1]
print(L)


# 1.用字符串s = "ABC"　和　s2 = "123",生成列表['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
s = "ABC"
s2 = "123"
L = [x + y for x in s for y in s2]
print(L)

# 2.有一些数存在于列表L中，如：L = [1,3,2,1,6,4,2...98,82]，将列表L中的数存入于另一个列表L2中
# 要求重复出现多次的数字只在L2列表中保留一份

L2 = []
L = [1, 3, 2, 1, 6, 4, 2, 12, 18, 21, 22, 82, 98, 82]
for x in L:
    if x not in L2:
        L2 += [x]      # L2.append(x)
print(L2)
print(L)

# 3.生成前40个斐波那契数(Fibonacci)1　1　2　3　5　8　13．．．(自第3个起，之后的所有数为前两个数之和)
# 要求将这些数保存在列表中，最后打印列表中的这些数

# 方法1
i = 3
L = [1, 1]
while True:
    L += [L[-2] + L[-1]]
    i += 1
    if i > 40:
        break
print(L)

# 方法2
L = [1, 1]
while len(L) < 40:
    L.append(L[-1] + L[-2])
print(L)

# 方法3
a = 0
b = 1
L = []
while len(L) < 40:
    a, b = b, a + b
    L.append(a)
print(L)
