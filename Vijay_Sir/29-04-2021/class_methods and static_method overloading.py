class A:

    @classmethod
    def personal(cls, name, phno, dob):
        return f'''User Name: {name},
phone Number: {phno},
Date Of Birth:{dob}'''

    @staticmethod
    def status(res):
        return f'''A class User Status is:{res} \n'''


class B(A):
    @classmethod
    def personal(cls, name, phno, dob):
        print(A.personal('Uday', 9703654029, '31-05-1998'))
        print(A.status('off_line'))
        return f'''Name: {name},
phone_number: {phno},
date Of Birth:{dob}'''

    @staticmethod
    def status(res):
        return f'''B class User Status is: {res}'''


b = B()
x = b.personal('XYZ', 7879798644, '15-02-2020')
print(x)
y = b.status('Online')
print(y)

# ----Code for dictionary Reversing and sorting ----

c = {'chuck': 1, 'annie': 42, 'jan': 100}
c1 = {}
for i, j in c.items():
    print(c1)
print(sorted([(v, k) for k, v in c.items()]))
