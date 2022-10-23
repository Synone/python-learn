 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
 
thisdict.update({"year":2020}) # update list 
# = thistdict["year"] = 2020
print(thisdict)
thisdict.update({"color":"red"}) # update 
#pop() method removes the item with the specified key name:
 
thisdict.pop("model")
print(thisdict['year'])
# del thisdict["model"] # del items with specified key
 

bob2 = dict(name="Sony", last_name="nguyen") # Zipping
print(bob2) #{'job': 'dev', 'name': 'Bob', 'age': 40}
#######
for k,v in thisdict.items():
  print(k,v)