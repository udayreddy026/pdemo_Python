class Father:
    def __init__(self):
        self.Father_Name = ''

    def Details(self):
        print('Father_name:', self.Father_Name)
        # return f'''Father Name:{self.Father_Name}'''


class Mother:
    def __init__(self):
        super(Mother, self).__init__()
        self.Mother_Name = ''


class Child(Father, Mother):
    def __init__(self):
        super(Child, self).__init__()
        self.Child_Name = ''

    def Details(self):
        super(Child, self).Details()
        return self.Child_Name


c = Child()
c.Father_Name = 'TvR'
c.Child_Name = 'Uday'
c.Mother_Name = 'Vimala'
print(c.Mother_Name)
print(c.Father_Name)
print(c.Child_Name)

print(c.Details())