#factorial  of the number 
num= int(input())
factorial=1

if num <0:
    print("sorry")
elif num==0:
    print("Sorry")
else:
    for i in range(1,num+1):
        factorial =factorial*i
    print("The factorial of the number",num,"is",factorial)