#Count the no. of occurences of a given item in a list.


def countocc(li,x):
    count=0
    for i in li:
        if i==x:
            count+=1

    return count


li=[10,20,30,40,50,60,40]
x=40
print(countocc(li,x))


