animal = "cow"
item = "moon"
number = 5200000
text = "The {} is riding over the {}."
print("The moment {} is over {}.".format(animal,item))
print(text.format(animal,item))
print("The moment {1} is over {1}.".format(animal,item))
print("The moment {0} is over {0}.".format(animal,item))
print("The moment {ani} is over {items}.".format(ani = "buffalo",items="sun"))
print("Hello my name is {:,}. I am {} super {}.".format(number,item,animal))
