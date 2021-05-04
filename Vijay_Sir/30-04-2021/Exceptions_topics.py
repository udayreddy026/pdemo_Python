# ----- Exception On list indexing ----

print("Hello   uday reddy syed anwar")
print("Hello")
x = [10, 20, 30, 40, 50]
print(x[2])
try:
    print(x[(int(input("Enter List index to access the list values...")))])
except IndexError:
    print("List Position not found Pls enter Correct Position")
print("Bye")
# print("Good Bye")


x = [10, 20, 30, 40, 0, -31]

print("Hai")
try:
    print(10/x[int(input("Enter list index to access number & Dividing"))])

    print(20/int(input("Enter a number denominator num::: ")))
except (ZeroDivisionError, IndexError):
    print("Invalid Number.... Dividing With Zero is infinity")
    print("Invalid Index number")


