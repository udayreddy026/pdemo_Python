x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 33, 39, 43, 53, 63, 73]

odd_count = 0
even_count = 0

for i in x:
    if i % 2 == 0:
        even_count = even_count + 1
    elif i % 2 != 0:
        odd_count = odd_count + 1

print(odd_count)
print(even_count)
