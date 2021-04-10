class Person:
    def __init__(self, list):
        # for z in range(0, len(list), 1): # Picking index values
    # def __init__(self, name, age, gender, phone, aadhaar):
        self.p_name = list[0]
        self.p_age = list[1]
        self.p_gender = list[2]
        self.p_phone = list[3]
        self.p_aadhaar = list[4]

    def details(self):
        p = f'Person name is: {self.p_name}\n Person age is:{self.p_age}\n Person Phone Number:{self.p_phone}\n Person Gender is:{self.p_gender}\n' \
            f'Person Aadhaar Number:{self.p_aadhaar}\n'
        print(p)


person_info = ['name', 'age', 'gender', 'phone', 'aadhaar']
person_details = []

for a in person_info:
    if a == 'name':
        name = input("Enter Person name:")
        person_details.append(name)
    elif a == 'age':
        age = int(input("Enter Person age:"))
        person_details.append(age)
    elif a == 'gender':
        gender = input("Enter Person gender:")
        person_details.append(gender)
    elif a == 'phone':
        phone = int(input("Enter Person Phone Number:"))
        person_details.append(phone)
    elif a == 'aadhaar':
        aadhaar = int(input("Enter Person Aadhaar Number:"))
        person_details.append(aadhaar)

p1 = Person(person_details)
p1.details()





