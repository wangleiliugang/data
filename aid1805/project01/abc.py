# s = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         s += i
# print(s)




s = 0
i = 1

while True:
    if i >100:
        break
    if i % 2 == 0:
        s += i
        i += 1
    i += 1
print(s)



s += i ---> s = s + i
i += 1 ---> i = i + 1
