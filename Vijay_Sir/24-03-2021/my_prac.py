# i = 1500
# while i <= 2700:
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#     i = i + 1

# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]
#
# if i_convention.upper() == "C":
#     result = int(round((9 * degree) / 5 + 32))
# #     o_convention = "Fahrenheit"
# # elif i_convention.upper() == "F":
# #     result = int(round((degree - 32) * 5 / 9))
# #     o_convention = "Celsius"
# # else:
# #     print("Input proper convention.")
# #     quit()
# # print("The temperature in", o_convention, "is", result, "degrees.")
# print(result)


temp = input("Enter the temperature you like to convert? ")
degree = int(temp[:-1])
covert = temp[-1]

if covert == "c":
    res = int(round((9 * degree + (32 * 5))/5))
    o_c = "F"

elif covert == "f":
    res = int(round((5 * (degree - 32))/9))
    o_c = "C"
print("The temperature in", o_c, "is", res)