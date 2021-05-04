def basic_salary(x):
    if x <= 10000 or x <= 20000 or x > 20000:
        return x


def da(basic_salary, da):
    return basic_salary * da / 100


def hra(basic_salary, hra):
    return basic_salary * hra / 100


a1 = basic_salary(10000)
print("Basic_salary", a1)
b1 = da(a1, 80)
print("DA", b1)
c1 = hra(a1, 20)
print('hra', c1)

Gross_salary1 = a1 + b1 + c1
print("Gross_salary1 = ", Gross_salary1)
print()

a2 = basic_salary(20000)
print("Basic_salary", a2)
b2 = da(a2, 90)
print("DA", b2)
c2 = hra(a2, 25)
print('hra', c2)

Gross_salary = a2 + b2 + c2
print("Gross_salary = ", Gross_salary)
print()

a3 = basic_salary(210000)
print("Basic_salary", a3)
b3 = da(a3, 95)
print("DA", b3)
c3 = hra(a3, 30)
print('hra', c3)

Gross_salary3 = a3 + b3 + c3
print("Gross_salary3 = ", Gross_salary3)
