s1 = 'Hello Programmer Welcome to wold'
l1 = s1.split(" ")
# print(l1)

for words in l1:
    for j in range(len(words) - 1, -1, -1):
        print(words[j], end="")
    print(" ", end="")

