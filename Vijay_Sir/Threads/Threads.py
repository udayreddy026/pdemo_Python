from threading import Thread,current_thread
import time


class Th(Thread):
    def run(self):
        time.sleep(3)
        for i in range(1,256):

            print(chr(i))


t = Th()
t.start()
print(current_thread(),"is sleeping for 3 sec")
time.sleep(3)
print("sleep completing")
for i in range(1,1000):
    print(i)
