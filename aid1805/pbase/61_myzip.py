# 此示例示意zip函数的内部实现机制

def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        x = next(it1)  # 可能会触发StopIteration
        y = next(it2)  # 可能会触发StopIteration
        yield (x, y)

numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for x in myzip(numbers, names):
    print(x)


# 1.写一个程序，读入任意行的文字，当输入空行时结束输入.打印带有行号的输入结果
# 如：请输入：hello<回车>
   # 请输入：world<回车>
   # 请输入：bye<回车>
   # 请输入：<回车>
   # 打印如下:
   # 第1行：hello
   # 第2行：world
   # 第3行：bye
def get_lines():
    L = []
    while True:
        s = input("请输入一段文字：")
        if not s:
            return L
        L.append(s)
    return L

# 方法1
def print_text(lst):
    for numbers, text in enumerate(lst, start=1):
        print('第', numbers, '行:', text)

if __name__ == '__main__':
    print_text(get_lines())



# # 方法2
# L = get_lines()
# for numbers, text in enumerate(L, start=1):
#     print('第', numbers, '行:', text)
