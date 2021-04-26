# ---- Add Method In SETS ----

print(dir(set))
print(help(set.add))
x = {10, 20, 'Uday', 30}
print(x)
x.add('Reddy')
print(x)
x.add(10)
print(x)

# ---- CLEAR METHOD IN SETS ----
print(dir(set))
print(help(set.clear))
x = {10, 20, 'Uday', 30}
x.clear()
print(x)

# ---- COPY METHOD IN SETS ----
print(dir(set))
print(help(set.copy))
x = {10, 20, 'Uday', 30}
y = x.copy()
print('set of Y Values:::', y)
print('set of X Values:::', x)

# ---- DIFFERENCE METHOD IN SETS ----

print(dir(set))
print(help(set.difference))
x = {10, 20, 'Uday', 30, 7.0}
y = {'Uday', 3.0, 10, 30, 20}
a = {20, 'dddddd'}
z = x.difference(y, a)
print(z)

# ---- DIFFERENCE_UPDATE METHOD IN SETS ----

print(dir(set))
print(help(set.difference_update))
x = {10, 20, 'Uday', 30, 7.0}
y = {'Uday', 3.0, 10, 30, 20}
a = {20, 'dddddd'}
y.difference_update(a)
print(y)

# ---- DISCARD METHOD IN SETS ----

print(dir(set))
print(help(set.discard))
x = {10, 20, 'Uday', 30, 7.0}
y = {'Uday', 3.0, 10, 30, 20}
a = {20, 'dddddd'}
x.discard('Uday')
print(x)

# ---- INTERSECTION METHOD IN SETS ----

print(dir(set))
print(help(set.intersection))
x = {10, 20, 30, 40}
y = {50, 60, 70, 80, 90}
a = {20, 'dddddd'}
z = x.intersection(a)
print(z)

# ---- INTERSECTION_UPDATE METHOD IN SETS ----

print(dir(set))
print(help(set.intersection_update))
x = {10, 20, 30, 40}
y = {50, 60, 70, 80, 90, 10, 20}
a = {20, 'dddddd'}
x.difference_update(y)
print(x)

# ---- ISDISJOINT METHOD IN SETS ----

print(dir(set))
print(help(set.isdisjoint))
x = {10, 20, 30, 40}
y = {50, 60, 70, 80}
z = x.isdisjoint(y)
print(z)

# ---- ISSUBSET METHOD IN SETS ----

print(dir(set))
print(help(set.issubset))
x = {10, 20, 30, 40}
y = {10, 20, 30, 40}
z = x.issubset(y)
print(z)

# ---- POP METHOD IN SETS ----
print(dir(set))
print(help(set.pop))
x = {10, 20, 30, 40}
y = {10, 20, 30, 40}
z = x.pop()
x1 =x.pop()
print(z)
print(x1)

# ---- REMOVE METHOD IN SETS ----
print(dir(set))
print(help(set.remove))
x = {'Uday', 10, 20, 30, 40}
y = {10, 20, 30, 40}
x.remove(10)

x.remove('Uday')
print(x)

# ---- symmetric_difference METHOD IN SETS ----
print(dir(set))
print(help(set.symmetric_difference))
x = {'Uday', 10, 20, 30, 40}
y = {10, 20, 30, 40}
z = x.symmetric_difference(y)
print(z)

# ---- symmetric_difference_update METHOD IN SETS ----
print(dir(set))
print(help(set.symmetric_difference_update))
x = {'Uday', 10, 20, 30, 40}
y = {10, 20, 30, 40}
x.symmetric_difference_update(y)
print(x)

# ---- union METHOD IN SETS ----
print(dir(set))
print(help(set.union))
x = {'Uday', 10, 20, 30, 40}
y = {90, 80, 70, 60}
z = x.union(y)
print(z)

# ---- UPDATE METHOD IN SETS ----
print(dir(set))
print(help(set.update))
x = {'Uday', 10, 20, 30, 40}
y = {90, 80, 70, 60,10, 20}
x.union(y)
print(x)
print(y)

