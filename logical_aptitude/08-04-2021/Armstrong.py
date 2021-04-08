# # Armstrong Number means number ex:153  = 1cub+5cub+3cub = same as give number is called armstrong
#
# num = 153
# temp = num
# arm_total = 0
# while num > 0:
#     l_num = num % 10
#     num = num // 10
#     arm_total = arm_total+(l_num**3)
# # print(arm_total)
#
# if arm_total == temp:
#     print(arm_total, "is armstrong")
# else:
#     print(arm_total, "is not armstrong")
#
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in x:
#     print(i)
for i in range(len(x)-1, -1, -1):
    print(x[i])
print()
for i in range(0, len(x), 2):
    print(x[i])