num = int(input("Enter a Number::"))

temp = num

res = 0

while num > 0:
    last = num % 10
    num = num // 10
    res = res + last
    # res = (res * 10) + last

div_res = temp // res
print(div_res)

# input number 36 and it will need sum of this number like 3 + 6 = 9 and dividing 36 / 9 = 4