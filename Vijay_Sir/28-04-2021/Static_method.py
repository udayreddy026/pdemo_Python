x = 20
y = 10

class Add:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def add(m, n):
        z = y + x
        a = n - m
        print('GLOBAL VARIABLES ACCESSING', z)
        print('Local VARIABLES ACCESSING', a)

    def sub1(self):
        return self.a * self.b


Add.add(50, 20)
a1 = Add(30, 40)
print(a1.sub1())
a1.add(10, 20)

