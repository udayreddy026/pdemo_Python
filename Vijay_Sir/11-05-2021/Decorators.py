
def dec_sample(x):
    def in_sample():
        print("****** Welcome to Decorators concept in python ******")
    return in_sample

@dec_sample
def sample():
    print("Welcome to Python Concepts....")


sample()





def add(z):
    def add_sum(x, y):
        return f'''sum of two numbers is {x+y}'''
    return add_sum


@add
def sub():
    print("Welcome")


a = sub(10, 20)
print(a)






def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


def decor3(func):
    def inner():
        x = func()
        return x * 3
    return inner


@decor1
@decor3
@decor
def num():
    return 10


print(num())