x = 'hello'
y = 'world'

if x[-1] == y[1]:
    print("True", x[-1], y[1])

    if len(x) != len(y):
        print("Both r equal!!!!!!")

    elif id(x) == id(y):
        print("Both The Id R equal!!!")
    else:
        print("No One conditions ")
else:
    print("Bye")


