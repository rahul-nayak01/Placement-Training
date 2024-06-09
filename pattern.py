#steps:
#1.see no. of rows & apply loop
#2.see no. of col & apply loop
#3.check for any relationship betn rows and col
#4.print req char
#5.check where to print space

n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()
    