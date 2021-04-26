class A:
    y = 20
    def __init__(self):
        self.x = 30

    def m1(self):
        self.x = self.x + self.x
        A.y = self.x + A.y


class B(A):
    # def __init__(self):
    #     self.x = 40

    def m1(self):
        A.x = self.x + A.x


# b = B()
# b.m1()
# # b.m1()
# print(A.x)

a = A()
a.m1()
print(A.y, a.x)

