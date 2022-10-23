class  Vehicle:
    color = None
class Car:
    color = None
class Motocycle:
    color = None


def change_color(vehicle,color):
    vehicle.color = color


vehi1 = Vehicle() # đối tượng của lớp Vehicle
car1 = Car() # đối tượng của lớp Car
bike1 = Motocycle() # đối tượng của lớp Motocycle
# object as arguments, đối tượng được sử dụng làm tham chiếu.

change_color(car1,"Blue")
change_color(vehi1,"Whatever it is")
change_color(bike1,"White")

print(vehi1.color)
print(bike1.color)
print(car1.color)