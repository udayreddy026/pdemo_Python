from abc import ABC,abstractmethod

class Numariccal(ABC):

    def add(self, a, b):
        print(self)
        return a + b

    def sub(self, a, b):
        print(self)
        return a - b

    @abstractmethod
    def mul(self, a, b):
        print(self)
        return a * b



class stringcal(Numariccal):
    def mul(self):
        print("We cant mul the to strings....")

s = stringcal()
print(s)
s.mul()


class GrandFather(ABC):

    def surname(self, sname):
        return f'''Grand father Surname is:::'''

    @abstractmethod
    def Fname(self,fname):
        return f'''First Name is:::'''


class father(GrandFather):
    def Fname(self,fname):
        return f'''first Name is {fname}'''


f = father()
print(f)

print(f.Fname('Venkatarathnam Reddy'))