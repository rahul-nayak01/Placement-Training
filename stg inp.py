#pgm to read stg from user and implement logic to remove character  which are at the odd no of index .

s=input("")
a=""
for i in range(0, len(s)):
    if i%2==0:
        a=a+s[i]
print(a)