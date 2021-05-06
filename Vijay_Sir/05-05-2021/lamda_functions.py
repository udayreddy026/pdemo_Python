# Syntax:
# function_name = lambda parameters : return values

add = lambda x, y: x + y

res = add(10, 20)
print(res)

odd_even = lambda x:'even' if x % 2 == 0 else 'odd'

x = odd_even(10)
print(x)
