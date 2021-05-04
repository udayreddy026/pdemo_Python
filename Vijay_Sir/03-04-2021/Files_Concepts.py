# # -------------------------- Reading File Concepts ------------------------
# f = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/demo.txt', 'r')
# a = f.read()
# print(a)
#
# # ----------------------- readline method -----------------------
# f = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/demo.txt', 'r')
# # a = f.readline()
# print(f.readline())
# print(f.readline())
# print(f.readline())
#
# # ---------------------- readlines method --------------------------
# f = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/demo.txt', 'r')
# a = f.readlines()
# print(a)
# print(a[2])
# print(a[1])
# print(a[0])
# for i in a:
#     print(i)

# -------------------------- Writing File Concept ---------------------------
# ---------- We can using write mode it will erases existing data in file ---------
# f = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/write.txt', 'w')
# v = f.writelines('uday')
# print(v)

f = open('E:/pdemo_Python/Vijay_Sir/03-04-2021/write.txt', 'a')
f.writelines('\n')
f.writelines('uday reddy')

