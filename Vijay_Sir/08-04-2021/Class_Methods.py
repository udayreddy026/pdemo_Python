class Fan:
    def rotating(self):
        print(self, "Moving")

    def stop(self):
        print(self, "Stopped")


f1 = Fan()
f2 = Fan()
f1.rotating()
f2.stop()
