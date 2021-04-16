s1 = 'palle'
s2 = 'apple'
total_mach = 0

for i in s1:
    for j in s2:
        if i == j:
            total_mach = total_mach + 1
            break

if total_mach == len(s1) and total_mach == len(s2):
    print("Anagram")
else:
    print("Is not Anagram")
