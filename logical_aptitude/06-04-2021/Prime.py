num = int(input("Enter a number:::"))
prime = True
i = 2
while i <= num-1:
    if num % i == 0:
        prime = False
        break
    i = i + 1

if prime == True:
    print(num, "is a prime")
else:
    print(num, "is a not prime")

num = int(input("Enter a number:::"))

# i = 2
# while i <= num-1:
#     if num % i != 0:
#         print(num, "is a prime number")
#         break
#     else:
#         print(num, "is a not prime number")
#     i = i + 1
#

