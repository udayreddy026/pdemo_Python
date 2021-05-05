x = [10, 2, 4, 5, 9, 20, 30, 40, 50, 60, 70]

sqr = [i ** 2 for i in x]

cub = [i ** 3 for i in x]

eve = [i for i in x if i % 2 == 0]

odd = [i for i in x if i % 2 != 0]

eve_sqr_odd_cub = [i ** 2 if i % 2 == 0 else i ** 3 for i in x]


print(sqr)
print(cub)
print(eve)
print(odd)
print(eve_sqr_odd_cub)

