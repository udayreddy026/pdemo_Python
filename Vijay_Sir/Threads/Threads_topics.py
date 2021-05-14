from threading import current_thread, Thread
import time


print(current_thread())

print("Hai")
print("Welcome")
time.sleep(3)
print(current_thread())
print("How Are You")
print("Bye")
time.sleep(3)
print("Gud Bye...")
print(current_thread())


# -------- Creating a custom own thread ----------

class Sample(Thread):
    def run(self):
        print('Welcome to run method in thread class')
        print(current_thread())


s = Sample()
s.start()

for i in range(1, 20):
    print(i)
print(current_thread())


class Demo(Thread):
    def run(self):
        print("Call the out said function...")
        time.sleep(5)
        global details
        details = gmail('udayreddy026@gmail.com', "UdayReddy")
        print(details)

    def iron(self, s):
        time.sleep(7)
        print(f'''Iron method string is: {s}''')

d = Demo()
d.start()
d.iron('Reddys')


def gmail(e_mai_id, name):
    return e_mai_id, name