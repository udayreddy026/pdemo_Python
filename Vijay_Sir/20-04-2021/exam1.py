# 1st Input a1b2c3d4e5f6
# 2nd Input only int

s = input("Enter String :")
d = int(input("Enter a number :"))
words = []
num = []
res1 = []
for i in range(0, len(s)-1, 2):
    words.append(s[i])
for j in range(1, len(s), 2):
    num.append(s[j])

for x in range(0, len(num)):
    for y in range(x, len(words)):
        while x >= 0:
            res1.append(words[y])
            # print(words[y], end="")
            x = x - 1
print(res1)
if d <= len(res1)-1:
    print(res1[d])
else:
    print("Pls Enter valid number")
