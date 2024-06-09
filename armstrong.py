#write a code in python to check if number is armstrong number.

num = int(input("Enter a number: "))

sum = 0
order = len(str(num))
temp = num
while(num!=0):
    digit = num % 10
    sum += digit **order
    num //= 10
if(sum==temp):
    print(f"{temp} is a armstrong number")
else:
    print(f"{temp} is not a armstrong number")
