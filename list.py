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

l1[1]="apple"
print(l1)
l1[1:3]=["Pineapple"]
         

#replace
list=["apple", "banana", "cheese"]
list[1:2]=["blackcurrent","watermelon"]
print(list)

list=["apple", "banana", "cheese"]
list[1:2]=["blackcurrent"]
print(list)


#insert
list=["apple", "banana", "cheese"]
list.insert(0, "blackcurrent")
print(list)


list=["apple", "banana", "cheese"]
list.append("blackcurrent")
print(list)


list=["apple", "banana", "cheese"]
l2=["blackcurrent"]
list.extend(l2)
print(list)

thislist=["apple", "banana", "cheese"]
del thislist[0]
print(thislist)

thislist1=["apple", "banana", "cheese"]
thislist1.clear()
print(thislist1)

#remove
thislist2=["apple", "banana", "cheese"]
thislist2.remove("banana")
print(thislist2)

#pop is also there.

thislist=["apple", "banana", "cheese"]
for i in range(len(thislist)):
    print(thislist[i])


thislist=["apple", "banana", "cheese"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1





