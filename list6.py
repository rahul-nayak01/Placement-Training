"""thislist=["apple", "banana", "cheese","Orange","Kiwi"]
thislist[0]="kiwi"
thislist[-1]="apple"
print(thislist)"""
#or

#swap functio 

def swaplist(li):
    size=len(li)
    temp=li[0]
    li[0]=li[size-1]
    li[size-1]=temp
    return li

li=[12,45,75,2,45]
print(swaplist(li))