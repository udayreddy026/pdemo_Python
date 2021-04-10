class Coffee:
    def __init__(self, c_name, c_fl, c_price = 20):
        self.coffee = c_name
        self.coffee_price = c_price
        self.coffee_fl = c_fl


c1 = Coffee('nowsad', 'chock')
c2 = Coffee("Uday", 'nik', 50)
print(c1.coffee, "is taking coffee price is", c1.coffee_price, "flaw is:", c1.coffee_fl)
print(c2.coffee, "is taking coffee price is", c2.coffee_price, "flaw is:", c2.coffee_fl)

