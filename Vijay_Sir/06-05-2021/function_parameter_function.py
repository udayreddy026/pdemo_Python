# def m():
#     print('Hello')
#
#
# def f(a):
#     a()
#
#
# f(m)

# def m1(a):
#     res = a(10)
#     print(res)
#
#
# def sqrt(num):
#     print(num ** 2)
#
#
# m1(sqrt)

# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def mul(x, y):
#     return x * y
#
#
# def div(x, y):
#     return x / y
#
#
# def main(fun, a, b):
#     res = fun(a, b)
#     print(res)
#
#
# main(add, 10, 30)
# main(sub, 60, 30)
# main(mul, 70, 20)
# main(div, 109, 8)
#
#
# def m11(a, b):
#     print(a(10) + b)
#
#
# def sqrt(num):
#     return num ** 2
#
#
# m11(sqrt, 10)

def upper(s):
    return s.upper()


def lower(s):
    return s.lower()


def capitalize(s):
    return s.capitalize()


def casefold(s):
    return s.casefold()


def endswith(s, s1):
    return s.endswith(s1)


def tabsize(s):
    return s.expandtabs(tabsize=2)


def find(s, s1):
    return s.find(s1)


def main_a(fun, s):
    res = fun(s)
    print(res)


def main_a1(fun, s, s1):
    res = fun(s, s1)
    print(res)


main_a(upper, 'uday')
main_a(lower, 'uDAy')
main_a(capitalize, 'uDAy reddy wew kejkjm kxdjgxl dkfgjkdgmksf ')
main_a(casefold, 'uDAy')
main_a(tabsize, 'Abcd efg hij klm nop qrs')

main_a1(endswith, 'udayreddy', 'y')
main_a1(find, 'Hello welcome to python programming in palle technologies.', 'palle')


print(dir(str))
print(help(str.format))

