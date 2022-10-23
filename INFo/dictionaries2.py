# NESTED DICTIONARIES
rec = {"name":{"first":"Bob","last":"Smith"},
"job": ["dev","mgr"],"age":40.5}
#print(rec["name"]) #{'first': 'Bob', 'last': 'Smith'}
#print(rec["name"]["first"]) #Bob
#print(rec["name"]["last"]) #Smith
#print(rec["job"][1]) #mgr => index trong list
#print(rec["job"])
#rec["job"].append("Janitor") # value của job là list, nên dùng append method cho list được
#print(rec)
#rec = 0
#print(rec)
animal ={"Prey":{"Land":["Deer","Rabbit","Cow","Baby zebra","Horse"],"Sea": ["Small fish","Sea lion","Penguin"]},
"Predator": {"Land":["Tiger","Lion","Cheetah","Jaguar"],"Sea":["Whale","Shark","Dolphin"]},
"Both": "Fish"
}
print(animal["Prey"]["Land"][3])
print(animal["Predator"]["Sea"][2])
print(animal["Prey"].items())
for a,b in animal["Prey"].items():
    print(a,b)