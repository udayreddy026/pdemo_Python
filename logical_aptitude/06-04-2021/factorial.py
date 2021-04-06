# Using While Loop
num = int(input("Enter a number:"))
fact = 1
i = 1
if num > 1:
    while i <= num:
        fact = fact*i
        i = i + 1
print(fact)

# Using For Loop

num = int(input("Enter number:"))
fact = 1
if num > 1:
    for i in range(1, num+1):
        fact = fact * i

print(fact)