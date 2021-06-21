# 写一个类Bicycle　(自行车)类，有run方法，调用时显示骑行里程km
# class Bicycle:
#     def run(self, km):
#         print("自行车骑行了", km, "公里")
# 再写一个类EBicycle(电动自行车)类，在Bicycle类的机车上添加电池电量volume属性
# 有两个方法：1.fill_charge(self, vol) 用来充电，vol为电量
#           2.run(km) 方法每骑行10km消耗电量1度，同时显示当前电量，当电量耗尽时，则调用Bicycle的run方法骑行
#           class EBicycle(Bicycle):
#             ...

# b = Bicycle()
# b.run(10)  # 自行车骑行了10公里
# e = EBicycle(5)
# e.run(10)  # 电动车骑行了10公里
# e.run(100)  # 电动车骑行了40公里，自行车骑行了60公里
# b.fill_charge(10)
# b.run(100)


class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, "公里")

class EBicycle(Bicycle):
    def __init__(self, vol):
        self.vol = vol  # 用来记录电量

    def run(self, km):
        e_km = min(self.vol * 10, km)  # 电动的总数和骑行km公里数，取最小值
        if e_km > 0:
            print("电动骑行了", e_km, "公里")
            self.vol -= e_km / 10
        km -= e_km
        if km > 0:
            super().run(km)
        print("本次剩余电量是：", self.vol)
    # def run(self, km):
    #     e_km = self.vol * 10
    #     q_km = km
    #     if e_km > q_km:
    #         self.vol -= q_km / 10
    #         print("电动骑行了", q_km, "公里", "剩余电量是：", self.vol)
    #     else:
    #         print("电动骑行了", e_km, "公里", end=";")
    #         s = q_km - e_km
    #         super().run(s)
    #         self.vol = 0
    #         print("本次剩余电量为0！")

    def fill_charge(self, volume):
        self.vol += volume

b = Bicycle()
b.run(10)  # 自行车骑行了10公里
e = EBicycle(5)
e.run(10)  # 电动车骑行了10公里
e.run(100)  # 电动车骑行了40公里，自行车骑行了60公里
e.fill_charge(10)
e.run(90)