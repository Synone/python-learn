# Duck typing = concept where the class of an object is less important
#  than the methods/ attributes
#  class type is not checked if minimum methods/atrributes are present 

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwackking")
class Chick:
    def walk(self):
        print("This chick is walking")
    def talk(self):
        print("This chick is chicking")
    def sit(self):
        print("The chick is sitting")
class Dog:
    def walk(self):
        print("The dog is jumping")
    def talk(self):
        print("The dog is sleeping")
    def sit(self):
        print("The dog is sitting")
class Person():
    def catch(self,d): # use method of other class as argument, 
        d.walk() # as long as the class has walk method
        d.talk()
        d.sit()
        print("u caught the critter!")

duck = Duck()
chicken = Chick()
person = Person()
dog = Dog()

# person.catch(duck)  --->  'Duck' object has no attribute 'sit'
person.catch(chicken)