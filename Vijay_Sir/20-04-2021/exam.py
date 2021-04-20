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