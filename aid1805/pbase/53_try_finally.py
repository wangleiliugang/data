# 此示例示意try-finally 语句

def fry_egg():
    print("打开天然气并点燃")
    try:
        count = int(input("请输入鸡蛋个数："))
        print("煎蛋完成，共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天然气")

fry_egg()





def fry_egg():
    print("打开天然气并点燃")
    try:
        count = int(input("请输入鸡蛋个数："))
        print("煎蛋完成，共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天然气")

try:
    fry_egg()
except:
    print("程序已转为正常状态")