def swap_numbers(a,b):
    print("Before swapping:")
    print("a=",a)
    print("b=",b)
    a=a+b
    b=a-b
    a=a-b

    print("After swapping:")
    print("a=",a)
    print("b=",b)
    return a,b

num1=int(input())
num2=int(input())
num1,num2= swap_numbers(num1,num2)