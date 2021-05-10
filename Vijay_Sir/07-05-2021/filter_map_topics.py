# ---- Lambda function importance ----
def main(fun, x):
    return fun(x)


result = main(lambda x: "Even" if x % 2 == 0 else "Odd", 123)
print(result)


# ------Filter_Topics------
# filter method can take 2 paraeters one is function and another one is iterables

x = [10, 2, 4, 6, 7, 349, 23, 56, 46, 34, 899, 78, 44, 78, 33, 54, 30]

res_filter = list(filter(lambda i: i if i % 2 == 0 and i % 6 == 0 else None, x))
print("Divisible by 2 and 5 numbers is: ", res_filter)


# ---- filter_topic_example ----
x = [10, 2, 4, 6, 7, 349, 23, 56, 46, 34, 899, 78, 44, 78, 33, 54, 30]
res = tuple(filter(lambda i: i if i % 12 ==  0 else None, x))
print(res)


# ---- Filter_topics_Strings_examples ----

str1 = ['uday', 'reddy', 'shalini', 'poornaprakash', 'lakshminarayanreddy', 'lol']
rest = tuple(filter(lambda s: (s == ''.join(reversed(s))), str1))
print(rest)


# ---- Maping topics ----
z = [3, 5, 7, 21, 14, 16, 26]

res = list(map(lambda x: x if x % 2 == 0 else None, z))

print(res)

