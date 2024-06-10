#sort based on how close no is to 50.
#customize sort.

def fun(n):
    return abs(n-50)

thislist=[100,50,65,23,89,56,32]
thislist.sort(key=fun)

print(thislist)