str1 = 'Palle Technologies'
rev = ''
for revs in range(len(str1)-1, -1, -1):
    rev = rev + str1[revs]
print(rev)

if rev == str1:
    print("Is a Palindrome")
else:
    print("Is not a palindrome")
    # print(revs)