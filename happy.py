def ishappy(n):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r**2
        n=n//10
    return sum

num=int(input())
res=num

while (res!=1 and res!=4):
    res=ishappy(res)
    
if (res==1):
    print(f"{num} is happy no.")
elif (res==4):
    print(f"{num} is not happy no.")