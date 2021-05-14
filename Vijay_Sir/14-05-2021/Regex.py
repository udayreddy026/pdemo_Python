import re

# ---------- Gmail Pattern Matching Code ----------
ptr = "^[a-z0-9][\\w\\d]*@gmail\.com$"
str = 'udayreddy026@gmail.com'
res = re.match(ptr, str)
print(res)

# ---------- Reading File and Getting Matched Indian Phone Numbers data -----------
file = open('E:/pdemo_Python/Vijay_Sir/14-05-2021/Sample', 'r')
ptr = "[6-9][0-9]{9}"
x = file.read()
res = re.findall(ptr, x)
print(res)
