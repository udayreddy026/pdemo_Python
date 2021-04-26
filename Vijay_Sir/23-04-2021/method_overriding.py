class Trr:
    def __init__(self):
        self.house = '1flower'
        self.bike = 'No-Bike'
        self.mobile = 'No-Mobile'

    def details(self):
        return f'{self.house} house, {self.bike} bike, {self.mobile} mobile'


class Tvr:
    z = 'Uday'
    
    def __init__(self):
        self.house = '1flower'
        self.bike = 'CD-100'
        self.mobile = 'Redmi 6'

    def details(self):
        return f'{self.house} house, {self.bike} bike, {self.mobile} mobile'


class Uday(Trr, Tvr):
    def details(self):
        self.house = ' 2flowers '
        return f'{self.house} house, {self.bike} bike, {self.mobile} mobile {Tvr.z} '


u = Uday()
print(u.details())