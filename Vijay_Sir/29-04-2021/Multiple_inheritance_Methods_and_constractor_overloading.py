class GrandFather:
    def __init__(self):
        self.g_assets = 'House'

    def info(self):
        return f'''Grand Father Assets : {self.g_assets}'''


class Father:
    def __init__(self):
        super(Father, self).__init__()
        self.f_assets = 'Bike'

    def info(self):
        print(super(Father, self).info())
        return f'''Father Assets : {self.f_assets}'''


class Child(Father, GrandFather):
    def __init__(self):
        super(Child, self).__init__()
        self.c_assets = ''

    def info(self):
        print(super(Child, self).info())
        return f'''Child Assets : {self.c_assets}, {self.f_assets}, {self.g_assets}'''


c = Child()
c.c_assets = 'Car'
print(c.info())
