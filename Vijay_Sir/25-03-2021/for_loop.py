# Printing Dictionary Keys & Values!!!

x = {'a': 'apple', 'b': 'Ball', 'c': 'Cat', 'd': 'Dog', 'e': 'Elephant'}

for i in x:
    print(i, x[i])


# Printing 5,4,3,2,1
for i in range(5, 0, -1):
    print(i, end=" ")
# Printing 1,2,3,4,5
for i in range(0, 6):
    print(i)


# Printing Odd Numbers
x = [10, 11, 12, 23, 54, 43, 32, 1, 5, 98, 45, 44, 80]

for i in x:
    if i % 2 != 0:
        print(i)


# Printing 0, 0.5, 1, 1.5, 2, 2.5
x = [0, 0.5, 1, 1.5, 2, 2.5]

i = 0
while i <= 2.5:
    print(i)
    i = i + 0.5


# Printing
"""
*
**
***
****
*****
"""
num = int(input("How Many Rows U Need ::: "))

for i in range(0, num+1):
    for j in range(i+1):
        print("*", end=" ")
    print("")
