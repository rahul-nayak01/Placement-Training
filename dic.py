thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisdict2= dict(name="John", age = 36, country="United States")
print(thisdict)

#creating empty dict
my_dict = {}

#adding key value pairs to the dictionary

my_dict["name"] = "John"
my_dict["age"] = 36
my_dict["country"] = "Newyork"

print(my_dict)
print(len(my_dict))
print(type(my_dict))

#accessing the dictionary

print(my_dict['name'])
print(my_dict['age'])
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)
m=my_dict.get("city")
print(m)

for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])

#iteration over keys
print("keys:")
for key in my_dict.keys(): 
    print(key) 

#iteration over values
print("values:") 
for value in my_dict.values():
    print(value)

#iteration key-value pairs
print("key-Value PAirs:")
for key,value in my_dict.items():
    print(key,".",value)

#check if key exist
if 'name' in my_dict:
    print("'name' exists in dict")
else:
    print("'name' is not in dict")

my_dict['age']=35
print("Modified Age: ",my_dict['age'])

my_dict.update({"age":45})

#add to dict
my_dict['color1']="fair"
print(my_dict)

my_dict.update({"color2":"dark"})
"""
#remove key-value pair
removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
"""

#nested dictionary
my_fam={
    "child1": {
        "name": "Email",
        "year": "2015",
    },
    "child2": {
        "name": "Tobi",
        "year": "2015",
    },
    "child3": {
        "name": "linus",
        "year": "2015",
    }        
}

print(my_fam)
print(my_fam["child2"]["name"])

for i,obj in my_fam.items():
    print(i)
    for y  in obj:
        print(y +":",obj[y])

