# ALL ABOUT SET
thisset = {"apple", "banana", "cherry"}
# add by add() function
thisset.add("orange")
print(thisset) #{'apple', 'orange', 'banana', 'cherry'}

# add set into set use update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"} 

thisset.update(tropical)
print(thisset) #{'papaya', 'banana', 'cherry', 'pineapple', 'apple', 'mango'}

# add list into set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


# use remove or discard method to delete object in set
thisset.discard("banana") # will not raise an error 
thisset.remove("apple") #raise an error of the item does not exist

# join 2 set using update() and union()
set1 = {"a","b","c"}
set2 = {1,2,3}
# union returns #
# a new set containing all items from both sets
set3 = set1.union(set2)
  #{'a', 1, 2, 3, 'c', 'b'}
# the update() method #
# that inserts all the items from one set into another:
set1.update(set2)
print(set3)  #{'a', 1, 2, 3, 'c', 'b'}
print(set1)  #{'a', 1, 2, 3, 'c', 'b'}

#intersection_update() method #
#will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # trả kết quả là apple, vì chỉ có apple tồn tại trong cả 2 set

#The intersection() method will return a new set, #
# that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) #{'apple'}

print(z) #intersection trả một set riêng biệt chỉ chứa items tồn tại trong 2 sets  {'apple'}
#symmetric_difference_update() method will keep only the elements#
#  that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) #{'microsoft', 'banana', 'google', 'cherry'}
print(x)

#symmetric_difference() method will return a new set, #
# that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

