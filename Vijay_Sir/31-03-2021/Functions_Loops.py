# Checking Even or Odd!!!

def Even_Odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


a = Even_Odd(10)
print("Given Numbers is", a)


# Biggest of two numbers!!!

def big(a, b):
    if a > b:
        return 'A is big', a
    elif a < b:
        return 'B is big', b
    else:
        return "Both are equal!!!"


c = big(10, 30)
print(c)

# Taking Input from user and checking if is even or odd, If is even then print power of the even number and if it's
# odd print cube of odd number

def eo(num1):
    if num1 % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


num = int(input("Enter the number:::"))
res = eo(num)
print("The given number is ", res)
if res == 'Even':
    print("Power of given number is", num ** 2)
else:
    print("Cube of given number is", num ** 3)


# Take list as input and sum the list values and return the sum value!!!

def List_Sum(i):
    total = 0
    for i in i:
        total = total + i
    return total


x = [10, 20, 30, 40]

a = List_Sum(x)
print(a)


