class Pen:
    def write(self, lines):
        print(self, 'is writing', lines, 'lines')

    def refill(self, ink_ml):
        print(self, 'is refiling with', ink_ml, 'ml')

    def type(self, modal, color):
        print("pen modal is", modal, "& Color is ", color)


p1 = Pen()
p2 = Pen()
p3 = Pen()
p4 = Pen()

p1.write(10)
p2.refill(20)
p3.write(50)
p4.type('classmate', 'Blue')


