# Prime Or Not............!


num = int(input("Enter a number:::"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Is Not a Prime Number!!!", num)
            break
    else:
        print("Is a prime number", num)


# Swapping Dictionary Keys to Values And Values to Keys!!!!

x = {'one': 1, 'two': 2, 'three': 3}
x1 = {}
for k, v in x.items():
    x1[v] = k
print(x1)
