
#tuples are immutable, tuples start with () while list start with []
#print(coordinates[0])
friends = ("Michael", "Jim", "Pam", "Ryan", "Toby", "Dwight", "Oscar", "Kevin") #tuples
 
# add tuple with tuple
thistuple = ('apple','banana','cherry')
y = ('orange','durian',)
z = (1,2,3,4,)
thistuple +=z
# print(thistuple) = ('apple', 'banana', 'cherry', 'orange', 'durian', 1, 2, 3, 4)
# convert to list to add, same with delete tuple
thistuple1 = ("apple", "banana", "cherry")
y = list(thistuple1)
y.append("orange")
thistuple1 = tuple(y) 

#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#If the asterisk(*) is added to another variable name than the last, #
# Python will assign values to the variable #
# until the number of values left matches #
# the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# join 2 tuple by using the +
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3 = tuple1+tuple2
# multiply by *
tuple4 =tuple1*3
print(tuple4)
# count object in tuple
x = tuple4.count("a")
print(x) # có 3 a trong tuple4

tup = (i for i in range(10) if i%2 == 0)
a = tuple(tup)
# print(a) => (0,2,4,6,8)




