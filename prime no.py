start=int(input("enter start no"))
end=int(input("enter end no"))
count=0
for num in range(start,end+1):

    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        count=count+1
print("Total prime no in given range is=",count)
