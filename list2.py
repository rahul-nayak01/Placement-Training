#comprehend (in one place).

"""thislist=["apple", "banana", "cheese"]
for i in range(len(thislist)):
    print(thislist[i])


thislist=["apple", "banana", "cheese"]
[print(x) for x in thislist]    

thislist=["apple", "banana", "cheese"]
[print(thislist[i]) for i in range(len(thislist))] """

"""
fruits=["apple", "banana", "cheese","Kiwi","mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

    print(newlist)
    """

fruits=["apple", "banana", "cheese","Kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

