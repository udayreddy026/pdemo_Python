# print("Welcome")
# try:
#     file = open('E:/pdemo_Python/Vijay_Sir/04-05-2021/uday.txt', 'r')
#
#     file1 = open('E:/pdemo_Python/Vijay_Sir/04-05-2021/uday.txt', '+a')
#
#     file1.writelines('I am able to write in files ')
#     print(file.read())
#
#     x = file.readlines()
#     print(x[int(input("Enter index number:::"))])
#
#     file.close()
# except FileNotFoundError:
#     print("File is not found... Pls give correct file name")
#
# except IndexError:
#     print("Index is Not found....")
#
# print("File is closed......")


def reading_file():
    try:
        f = open('E:/pdemo_Python/Vijay_Sir/04-05-2021/uday1.txt', 'r')
        return f.read()

    except FileNotFoundError:
        print("File Not Existing in this directory")
    # finally:
    #     f.close()


def write_file(str):
    try:
        f = open('E:/pdemo_Python/Vijay_Sir/04-05-2021/uday1.txt', 'a')
        return f.writelines(str)
    except FileNotFoundError:
        print("File not found in this location so not able to edit this file")


v = reading_file()
# print(v)

write_file('gg')
print(v)
