n=int(input("Enter the number"))
fib1=0
fib2=1
print("enter a number in fibanocci series",n,"is")
print(fib1,fib2,end=" ")
for i in range(2,n):
    fib3=fib1+fib2
    print(fib3,end=" ")
    fib1=fib2
    fib2=fib3