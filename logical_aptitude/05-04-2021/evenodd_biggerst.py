# 3. Print Even or Odd
num = int(input("Enter a number:::"))
if num % 2 == 0:
    print("Its a even number:", num)
else:
    print("Its a odd number:", num)
    print()

# 4. Biggest to two numbers
x = int(input("Enter first number:::"))
y = int(input("Enter second number:::"))

if x == y:
    print("Both the number are equal...!")
elif x > y:
    print(x, "is big")
else:
    print(y, "is big")


# 5. Print 100, 99, 98,...........2,1,0 Using (While Loop)
i = 100
while i >= 0:
    print(i)
    i = i - 1

# 6. Print 0,5,10,15,20......100 using (while loop)
h = 0
while h <= 100:
    print(h)
    h = h + 5

# 7. Print -40, -38, -36, -34 ....... -22, -20 using (while loop)
h = -40
while h <= -20:
    print(h)
    h = h + 2

# 8. Print 1 to 100 numbers using (while loop)
# Follow the order all the numbers in single row separate with ,
a = 1
while a <= 100:
    print(a, end=",")
    a = a + 1

# 9. Print numbers in this order
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 11, 12, ..................,20
# ...........................100
b = 1
while b <= 100:
    print(b, end=",")
    if b % 10 == 0:
        print()
    b = b + 1#

# 10. Print 1,2,4,8,16,......2048
i = 1
while i <= 2048:
    print(i)
    i = i * 2

# 11. Print 100, 95, 90, 85.........,5,0
i = 100
while i >= 0:
    print(i)
    i = i - 5