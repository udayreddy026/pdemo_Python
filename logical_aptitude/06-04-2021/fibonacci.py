# Using While loop
num = int(input("Enter how many numbers u need:"))
x = 0
y = 1
total = 1
print(x)
print(y)
res = x + y
while total <= num:
# while total <= 20:
    print(res)
    x = y
    y = res
    res = x + y
    total = total + 1
# Using for loop
num = int(input("Enter how many numbers u need:"))
x = 0
y = 1
print(x)
print(y)
res = x + y
for i in range(1, num):
# while total <= 20:
    print(res)
    x = y
    y = res
    res = x + y