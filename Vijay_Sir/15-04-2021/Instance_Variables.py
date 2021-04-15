class Test:
    def __init__(self, x, y):
        self.a = x + y  # Instance Variable 'a'
        self.b = y - x  # Instance Variable 'b'


t = Test(10, 20)
print("X Value is:::", t.a)
print("y Value is:::", t.b)
