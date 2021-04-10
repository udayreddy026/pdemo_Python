x = []
n = int(input("Enter list length:"))
for i in range(0, n):
    le = int(input("Enter List elements:"))
    x.append(le)
# print(x)

large = x[0]

for items in x:
    if items > large:
        large = items

print(large, "Is Large number,")
print(x)
