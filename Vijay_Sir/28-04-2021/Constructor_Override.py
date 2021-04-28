class Example:
    def __init__(self):
        self.a = 'Sting Instance Variable'


class Ex:
    def __init__(self):
        super(Ex, self).__init__()
        self.b = 'Second Class Instance Variable'


class Ex1(Ex, Example):
    def __init__(self):
        super(Ex1, self).__init__()
        self.c = 'Ex1 Class Instance variable'
        self.a = 'Override Variable'

e = Ex1()
print(e.a)

print(e.b)
