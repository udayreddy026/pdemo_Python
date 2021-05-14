"""Private Variables not access out said of the class example program in below """

# class A:
#     x = 10
#
#     def __init__(self):
#         self.__x = 10
#         self.__s = 'Uday'
#
#     def details(self, status):
#         return status, self.x, self.s
#
#
# class B(A):
#     def cb(self):
#         self.x = 30
#
#
# a = A()
# z = a.details('Active')
# print(z)


""" How to get private Variables in outside of the class 
    using Get and set methods"""


# class A:
#     x = 10
#
#     def __init__(self):
#         self.__x = 10
#         self.__s = 'Uday'
#
#     def details(self, status):
#         return status, self.x, self.s
#
#     def setxs(self, x, s):
#         print(f'''Before __x Value is {self.__x}''')
#         self.__x = x
#         print(f'''After __x Value is {self.__x}''')
#         print()
#         print(f'''Before __s Value is {self.__s}''')
#         self.__s = s
#         print(f'''After __s Value is {self.__s}''')
#
#     def getxs(self):
#         return self.__x,self.__s
#
#
# class B(A):
#     def cb(self):
#         self.x = 30
#
#
# a = A()
# a.setxs(100, 'Welcome to get and set methods')
# z = a.getxs()
# print(z)


class Bank():
    def __init__(self, Account_number, Password):
        self.__Account_number = Account_number
        self.__Password = Password

    def ac_info(self, name, addres, phone_number, aadhar, amout):
        self.Name = name
        self.Address = addres
        self.PhNo = phone_number
        self.Aadhar_no = aadhar
        self.Amout = amout

        print(f'''Account Holder Name {self.Name}
        Address {self.Address}
        Phone Number {self.PhNo}
        Aadhaar Number {self.Aadhar_no}
        Amount Deposited : {self.Amout}''')


class New_branch(Bank):
    def New_branch_details(self, bank_name, banck_location, bank_ifsc, bank_phno):
        self.Bank_name = bank_name
        self.Bank_location = banck_location
        self.Bank_Ifsc = bank_ifsc
        self.Bank_phno = bank_phno

        return self.Bank_name, self.Bank_Ifsc, self.Bank_location, self.Bank_phno


n = New_branch(115810100079955, 5988)
n.ac_info('Uday', 'Chittoor', 9703654029, 711692771563, 10000)
