# total = 100
#
# country = "AU"
# if country == "AU":
#     if total <= 50:
#         print("Shipping Cost is  $50")
#     elif total <= 100:
#         print("Shipping Cost is $25")
#     elif total <= 150:
#         print("Shipping Costs $5")
#     else:
#         print("FREE")
#     if country == "AU":
#         if total <= 50:
#             print("Shipping Cost is  $100")
# else:
#     print("FREE")


rows = int(input("Enter how many rows u need"))

for i in range(1, rows+1):
    for j in range(i):
        print(i, end="")
    print()
