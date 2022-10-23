#name ="sonyne"
#if (name[0].islower()):
 #   name = name.capitalize()

# *args = parameter that will pack all arguments
# into a tuple useful so that a function can accept a varying amount of arguments
def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))

# kwargs: parameter that will pack all arguments into a dictionary

def hello(**kwargs):
    #print("Hello "+ kwargs["first"] +" "+kwargs["last"])
    print("Hello", end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")
    
hello(major = "Hacker",title = "Mr ",frist = "Bro",middle= "Nguyen",last ="Sony")


