class A:
    def m1(self):
        print("Hai")


class B(A):
    def m2(self):
        print("Hello")


class C(A):
    def m3(self):
        print("Welcome")


c = C()
c.m3()
c.m1()
