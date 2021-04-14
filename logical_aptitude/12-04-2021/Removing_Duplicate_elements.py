x = [10, 20, 30, 40, 50, 60, 10, 20, 40]

for i in range(len(x)):
    element_x = x[i]
    for j in range(i+1, len(x)):
        if x[j] == element_x:
            x[j] = -1


for z in range(len(x)):
    if x[z] != -1:
        print(x[z])

# y = set(x)
# print(y)
#
#
# z = tuple(y)
# print(z)

