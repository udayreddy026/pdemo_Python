x = 'Global Variable'


class Gl:
    y = 'CLass Variable'

    def __init__(self):
        self.name = 'Instance Variable'

    @classmethod
    def mw(cls, s):
        print(x)
        print(cls.y)
        print(s)


c = Gl()
c.mw(10)



