a = 10  # Global Variable


class A:
    def m1(self):
        b = 20  # Local Variable 'b'
        c = 30  # Local Variable 'c'
        print(b)
        print(c)
        print(a)

    def m2(self):
        print(a)


a1 = A()
a1.m2()
a1.m1()
