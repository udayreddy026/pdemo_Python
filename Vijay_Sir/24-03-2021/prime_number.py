num = int(input("Enter a number"))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime Number")
            break
        else:
            print("Is a prime number")
else:
    print("Is not prime number")

