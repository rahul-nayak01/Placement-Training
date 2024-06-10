#write a pgm to test list contains elements in a range.

li=[1,2,3,4,5,6,7,8,9,10]
a=int(input("Enter the range:"))
b=int(input("Enter the range:"))
for i in li:
    if i>=a and i<=b:
        print(i,end=" ")
