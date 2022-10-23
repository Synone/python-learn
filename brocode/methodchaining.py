# method chaining = calling multiple methods sequentially
# each call performs an action on the same object
# and return itself

class Car:
    def turn_on(self):
        print("You start the engine")
        return self # must have return the self.
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self #return 
    def turn_off(self):
        print("Engine off!")
        return self #return

car = Car()
car.turn_on().drive().brake().turn_off()
# above equal: car is self, after execute the code, 
# the previous code have to return the self to 
# continue the next code
car.turn_on()
car.drive()
car.brake()
car.turn_off()