#write a pgm to merge 2 sorted list into a single sorted list.

l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
m=[]
i=j=0
while(i<len(l1) and j<len(l2)):
    if l1[i]<l2[j]:
        m.append(l1[i])
        i=i+1
    else:
        m.append(l2[j])
        j=j+1
m.extend((l2[j:]))
m.extend((l1[i:]))
print(m)
    
