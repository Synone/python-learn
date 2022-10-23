smallest = None
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print(smallest)

largest = None
for value in [9,41,12,3,74,15]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    print(largest,value)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

num = 0 
tot =0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        continue
    num = num+1
    tot = tot + fval
print("ALL DONE")
print(tot,num,tot/num)