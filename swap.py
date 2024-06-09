#write a pgm to swap 2 numbers by using third variable.

def swap_numbers(a,b):
    print("Before swapping:")
    print("a=",a)
    print("b=",b)
    temp=a
    a=b
    b=temp

    print("After swapping:")
    print("a=",a)
    print("b=",b)
    return a,b

num1=int(input())
num2=int(input())
num1,num2= swap_numbers(num1,num2)