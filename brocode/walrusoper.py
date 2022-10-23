 
'''
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)'''
# print(happy=True) #'happy' is an invalid keyword argument for print()
print(happy:=True) # --> walrus operator
foods =list()
while food := input("What food do u like: ") != "quit":
    foods.append(food)
