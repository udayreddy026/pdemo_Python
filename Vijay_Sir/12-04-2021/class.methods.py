class Computer:
    def __init__(self, company, price, ram, hdd, os, processor):
        self.company = company
        self.price = price
        self.ram = ram
        self.hdd = hdd
        self.os = os
        self.processor = processor

    def assembling(self):
        print(f'''Assembling a new system with specifications is:
company Name :{self.company}
Cost :{self.price}
Ram :{self.ram}
Hard Disk Size :{self.hdd}
Operating system :{self.os}
Processor :{self.processor}''')

    def turn_on(self):
        print(f'''{self.company} is turned on''')

    def powerOff(self):
        print(f'''{self.company} is Shut Down''')


c1 = Computer('Dell', 34500, '4GB', '1TB', 'Windows 10 Home', 'i3 7thGen')
c2 = Computer('Lenovo', 30000, '6GB', '1.5TB', 'Windows 10', 'i5 11thGen')

c1.assembling()
c1.turn_on()
c1.powerOff()
print("********************************************************************")

c2.assembling()
c2.turn_on()
c2.powerOff()


