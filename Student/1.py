class transformstr(object):
    def __init__(self) -> None:
        self.s = ""

    def getString(self):
        self.s = input("Nhap mot cau ")
    def printString(self):
        a = self.s.upper()
        print(a)

def sqrnum(num):
    a = num**2
    print(a)
 
class Person:
    name = "Person"
    def __init__(self, name = None):
    # self.name là biến instance
        self.name = name

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))



