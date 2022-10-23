class Car:
    wheels = 4
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("The engine is started")
        print("The " + self.model + " is running." )
        return self
    def brake(self):
        print("Brake is on")
        print("The " + self.model +" is slowing down")
        return self
    def stop(self):
        print("The vehicle has stop")
        return self

