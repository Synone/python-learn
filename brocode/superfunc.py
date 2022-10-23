# super()= Function used to give asccess to the methods of a parent class.
# Returns a temporary object of a parent class when used

class Retangle:
    def __init__(self,length,width)  :
        self.length = length
        self.width = width

class Square(Retangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Retangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

squre = Square(3,3)
a = squre.area()
print(a)
cube = Cube(3,3,3)
c = cube.volume()
print(c)