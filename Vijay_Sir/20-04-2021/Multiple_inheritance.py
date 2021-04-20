class A:
    def m11(self):
        print('Hello i am Class A m11')


class B:
    def m22(self):
        print("Hello I am Class B M22")


class C:
    def m33(self):
        print("Hello I am class C M33")


class D(A, B, C):
    def m44(self):
        print("Hello I am class D M44")


d = D()
d.m11()
d.m22()
d.m33()
d.m44()

c = C()
c.m33()
