x = [10, 20, 30, 40, 50]
y = x
print(help(list.clear))
x.clear()
print(x)

# ----COPY METHOD----
print(dir(list))

print(help(list.copy))

x = [1, 2, 3, 4, 5]
y = x.copy()
print(x)
print(y)

# ----COUNT METHOD----
print(dir(list))
print(help(list.count))
x = [10, 20, 30, 40, 50, 60, 10, 40, 20, 20, 10]
y = x.count(10)
print(y)

# ----EXTEND METHOD----
print(dir(list))
print(help(list.extend))
x = [10, 20, 33, 22, 33, 55, 65, 332]

z = ['uday', 'poorna', 'shalini', 'LakshmiNaryanreddy']
x.extend('321')
y = [321]
x.extend(y)
x.extend('Uday')
print(x)

# ----INDEX METHOD----
print(dir(list))
print(help(list.index))

y = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
z = y.index(100)
print(z)

# ----INSERT METHOD----
print(dir(list))
print(help(list.insert))
y = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
y.insert(6, 'uday')
print(y)

# ---- POP METHOD ----
print(dir(list))
print(help(list.pop))
y = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
z = y.pop(3)
print(z)
print(y)

# ---- REMOVE METHOD ----

print(dir(list))
print(help(list.remove))
y = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
y.remove(10)
print(y)

# ---- REVERSE METHOD ----

print(dir(list))
print(help(list.reverse))
y = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100]
y.reverse()
print(y)

# ---- SORT METHOD ----
print(dir(list))
print(help(list.sort))
y = [1200, 110, 13, 190, 50, 60, 70, 80, 90, 100]
y.sort()
print(y)


