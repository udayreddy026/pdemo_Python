def fac(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact


num = int(input("Enter the number:::"))

print(fac(num))