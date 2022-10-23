n = 69

print(n.__add__(1))
print(n.__sub__(9))# tương tự n - 9
n.__mul__(2)# tương tự n * 2
n.__radd__(1) #tương tự 1 + n
n.__rsub__(9) # tương tự 9 - n
n.__neg__() # tương tự -n
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myFunc, ages)
for x in adults:
    print(x)