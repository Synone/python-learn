vowels =['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found ={}
 
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
    for k,v in sorted(found.items()):
        print(k, "was found", v , "times.")

   
 
nums = [1,4,3,5,6,7]
print(nums.pop(0))
####
a = [[n*5,n*5*2] for n in range(1,4)] # tạo công thức trong list
print(a)
b = [[n,n+1,n+2]for n in range(1,5)] #[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
print(b)