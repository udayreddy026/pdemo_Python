x = 'Uday'


class Ad:
    b = 90

    def __init__(self):
        self.z = 'Hello Method Instance variable'
        self.name = 'Instance Variable'

    def hello(self, ab):
        print(Ad.b)
        print(x)
        print(self.name)
        print(ab)
        print(self.z)


a = Ad()
a.hello(10)
