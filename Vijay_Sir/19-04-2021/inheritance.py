class Vehicle:
    def __init__(self, v_name, v_company_name, v_type, v_color, v_fuel_type):
        self.v_name = v_name
        self.v_company_name = v_company_name
        self.v_type = v_type
        self.v_color = v_color
        self.v_fuel_type = v_fuel_type

#     def v_details(self):
#         print(f'''Vehicle name is: {self.v_name}
# vehicle company name is: {self.v_company_name}
# vehicle type is : {self.v_type}''')
#         print(" ")


class Car(Vehicle):
    def car_details(self, cost):
        print(f'''Car Name is : {self.v_name}
Car Company is : {self.v_company_name}
Car type is : {self.v_type}
Car Color is: {self.v_color}
Car Fuel type is : {self.v_fuel_type}
Price of the car is:{cost}''')
        print(" ")


class Bike(Vehicle):
    def bike_details(self, cost, modal_number, cc, tank_capacity):
        return f'''
Bike Name is : {self.v_name}
Bike Company is : {self.v_company_name}
Bike type is : {self.v_type}
Bike Color is: {self.v_color}
Bike Fuel type is : {self.v_fuel_type}
Bike Model : {modal_number}
Bike CC : {cc}
Bike tank capacity : {tank_capacity}
Price of the bike is:{cost} \n'''


class Bus(Vehicle):
    def bus_details(self, modal_number, bus_setting_capacity, cost):
        return f'''
Bus name:{self.v_name}
Bus Company Name: {self.v_company_name}
Bus type is: {self.v_type}
Bus color is: {self.v_color}
Bus Fuel type is : {self.v_fuel_type}
Bus Mode Number: {modal_number}
Bus Setting capacity is :{bus_setting_capacity}
Bus cost is : {cost}
'''


c = Car('Audi', 'Audi', '4 Wheeler', 'Blue', 'Petrol')
c.car_details(100000)
c1 = Car("Benz", 'Benz', '4 Wheeler', 'Block', 'Petrol')
c1.car_details(4552154)
bike = Bike('Pulsar', 'Pulsar', '2 Wheeler', 'Block', 'Petrol')
print(bike.bike_details(150000, 5242, 220, '15Lts'))
bus = Bus('RBus', 'XYZ Company', '10 Wheeler', 'Green', 'Petrol & Gas')
print(bus.bus_details('B12345A', 70, 5000000))