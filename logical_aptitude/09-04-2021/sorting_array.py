
# Shorting an list elements

x = [10, 20, 50, 3, 2, 67]

# len = len(x)

for i in range(0, len(x)-1):
    for j in range(0, len(x)-i-1):
        if x[j] < x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]


print(x)
