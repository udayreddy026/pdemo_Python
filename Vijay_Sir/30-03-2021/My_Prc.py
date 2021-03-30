# Using loops in functions!!!!

def ar_op(x):
    for i in x:
        print(i)


x = [10, 20, 30, 40, 50]
x[3] = 'Uday'
x.append('Reddy')
x.insert(2, 100)

ar_op(x)


# Arbitrary Arguments is will take values like a tuple
def kids(*a):
    for i in a:
        print(i)


kids('Uday', 22, 'PoornaPrakesh', 21, 'shalini', 13, 'Lakshminarayan Reddy', 12, "\n")
kids('Uday1', 22.4, 'PoornaPrakesh', 21.4, 'shalini', 13.4, 'Lakshminarayan Reddy', 12.4, "\n")
kids('Uday2', 22.5, 'PoornaPrakesh', 21.5, 'shalini', 13.5, 'Lakshminarayan Reddy', 12.5, "\n")
kids('Uday3', 22.6, 'PoornaPrakesh', 21.5, 'shalini', 13.6, 'Lakshminarayan Reddy', 12.6, "\n")


# Using function given number Prime or nor !!!!

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i:
                print("Given number is not a Prime", num)
                break
            else:
                print("Given number id prime", num)
                break


prime(231)
