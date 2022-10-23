def simpleArraySum(ar):
    x = 0
    for i in ar:
        x = i+x
    return x
print(simpleArraySum([1,2,3,4,10,11]))