x = [10, 200, 322, 432, 622]

search_Element = 322
found = False

for i in range(0, len(x)):
    if x[i] == search_Element:
        print(i, "Element Position")
        found = True
        break


if found == "False":
    print(search_Element, "Element Position not found")

# x = [10, 20, 40, 50]
#
# for i in range(0, len(x)):
#     print(i)
