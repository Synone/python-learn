# Ma trận hay còn gọi là mảng hai chiều:
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[0][0])
print(a[1][1])
print(a[2][0])

print(a[2][2])
print(a[1][2])
print(a[0][2])
b = a.copy()

b.extend([[10,11,12],[13,14,15]])
print(b)

vowels =['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found ={}
found["a"] = 0
found["e"] = 0
found["i"] = 0
found["o"] = 0
found["u"] = 0
for letter in word:
    if letter in vowels:
        found[letter] +=1
    else:
        found[letter] = 1
for k,v in sorted(found.items()):
    print(k, "was found", v , "times.")