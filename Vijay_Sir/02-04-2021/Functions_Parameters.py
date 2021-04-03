# Positional Perameters...!!!

def positional(a, b):
    print(a)
    print(b)


positional(10, 20)


# Key Word arguments
def key_word(a, b, c):
    print("a :", a)
    print("b :", b)
    print("c :", c)


key_word(b=10, c=20, a=30)
key_word(10, c=50, b=30)


# Default Parameters
def default(a, c, d, b=10):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


default(10, 20, b=30, d=50)
default(10, c=20, d=100, b='Uday')
default(a=20, b=30, c=40, d=90)
default(a="Uday", b="Reddy", c="Tathi", d="Reddy")
default(a=10, b=20.3, c=[20, 30, 40], d={12, 1111113, 123123})


# Arbitrary Parameters

def arbitrary(*a):
    return a


c = arbitrary(10, 'Uday', 100101, 200)
for i in c:
    print(i)


