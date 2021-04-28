a = 20
b = 30


class Info:
    c = 40

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def add(cls):
        return a + cls.c

    @staticmethod
    def sub():
        return b - Info.c

    def mul(self):
        return self.x * self.y


print("Class Method... ", Info.add())
print('Static Method...', Info.sub())

i = Info(40, 50)
print(i.mul())

