def giaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
 
n = int(input("Nhập số nguyên dương n = "))
print("Giai thừa của", n, "là", giaithua(n))
# cách 2 giai thừa:

x = int(input("Nhập giai thừa:"))
def fact(x):
    if x ==0:
        return 1
    return x*fact(x-1)
print(fact(x))   


from itertools import permutations
# Get all permutations of [1,2,3] # hoán vị
perm = permutations([1,2,3])
# print the obtained permutations
for i in list(perm):
    print(i)
print(perm)
# get all permutations of length 2
# and length 2
perm = permutations([1,2,3],2)
# print the obtained permutations
for i in list(perm):
    print(i)


# A Python program to print all
# combinations of given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
	print (i)


# A Python program to print all combinations
# with an element-to-itself combination is
# also included
from itertools import combinations_with_replacement

# Get all combinations of [1, 2, 3] and length 2
comb = combinations_with_replacement([1, 2, 3], 2)

# Print the obtained combinations
for i in list(comb):
	print (i)
