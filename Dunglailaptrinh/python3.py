import turtle
import math
#bob = turtle.Turtle()
#for i in range(4):
   # bob.fd(100)
    #bob.lt(90)
    
def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
bob = turtle.Turtle()   
square(bob,200)

def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob,7,70)


# Circle
def circle(t,r):
    circumference = 2*math.pi*r
    n = 50
    length = circumference/n
    polygon(t,n,length)

circle(bob,100)








turtle.mainloop()