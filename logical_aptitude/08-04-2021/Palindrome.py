num = int(input("Enter a number:::"))
temp = num
res = 0
while num > 0:
    l_num = num % 10  # Getting Last number from user entered number its remainder
    num = num // 10   # Getting coefficient of number will become it means except last number remaining number will
# stored in num
    res = (res*10)+l_num
#print(res)

if temp == res:
    print(res, "Is palindrome Number")
else:
    print(res,"is not a palindrome number")
