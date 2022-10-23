smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
# In contrast, a data product is a technical functionality that encapsulates an algorithm and is 
# designed to integrate directly into core applications.

so = 1
print("Giai thừa của" )
for thing in range(1,int(input())+1):
    so = so*thing
    print(so,thing)
print("kết quả" + str(so))
