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