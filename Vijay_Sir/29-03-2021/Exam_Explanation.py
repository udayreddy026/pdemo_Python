# Prime or not..........

num = int(input("Enter a number:::"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Is not a prime number!!!!", num)
            break
        print("Is a prime number:", num)

# Swapping Dictionary keys to values and values to keys...
x = {'one': 1, 'two': 2, 'three': 3}

y = {}

for i in x:
    y[x[i]] = i
print(y)

# Packing and un-packing....
x = (10, 20, 30, 40)  # Is a packing

a, b, c, d = 10, 20, 30, 40  # Is not packing

x1 = (10, 20, 30, 40, 50, 60)

u, d, a, y, z, n = x1

print(u)
print(d)
print(a)
print(y)
print(z)
print(n)



