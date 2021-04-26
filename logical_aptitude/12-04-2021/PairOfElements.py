x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(x)):
    start_element = x[i]
    for j in range(i+1, len(x)):
        if start_element + x[j] == 100:
            print(f'pair of elements:{start_element},{x[j]}')

# l = []
# for i in range(1, 1245):
#     l.append(i)
#
# for x in range(len(l)):
#     start_ele = l[x]
#     for y in range(x+1, len(l)):
#         if start_ele + l[y] == 1245:
#             print(start_ele, l[y])
