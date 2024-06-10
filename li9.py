#find min and max element in list of elements without min and max built in function.
 
li=[23,44,66,22,78]

min=li[0]
for i in li:
    if i<min:
        min=i
        print(min)
    if i>max:
        max=i
        print(max)
    