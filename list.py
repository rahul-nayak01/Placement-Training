l1=[1,2,3,4,5]
l2=["apple", "orange","cherry","bannana"]
l3=[True,False]

l4=list(("Jack"))
l5=list(("Jack","John"))

print(l4)
print(l5)
print(l1[0])
print(l1[0:4])
print(l1[:4])
print(l1[0:])
print(l1[:])

#index less than range

print(l1[-4:-1])
print(l1[-1:-4])
x=len(l1)
print(x)
print(type(l1))
print(type(l1[0]))
if "apple" in l2:
    print("Exist")