# 1. Swapping two number using 3rd variable
a = 10
b = 20
temp = 0
print("Before Swapping a value is", a)
print("Before Swapping b value is", b)
print()
temp = a
a = b
b = temp
print("After Swapping a value is:", a)
print("After Swapping a value is:", b)

# 2. Swapping two number with out using 3rd variable
x = 100
y = 200
print("Before Swapping a value is", x)
print("Before Swapping b value is", y)
print()
x = x + y
y = x - y
x = x - y
# We can do like this also
# x, y = y, x
print("After Swapping a value is:", x)
print("After Swapping a value is:", y)
