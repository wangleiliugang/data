# 此示例示意在多继承中的方法查找顺序问题

class A:
    def m(self):
        print("A.m()")

class B(A):
    def m(self):
        print("B.m")
        super().m()  # 针对的是__mro__顺序来的

class C(A):
    def m(self):
        print("C.m")

class D(B, C):
    def m(self):
        print("D.m")
        super().m()

d = D()
d.m()

for x in D.__mro__:
    print(x)
    