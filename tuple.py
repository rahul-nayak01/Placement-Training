#tuple
def create_tuples():
    tuple1= (1,2,3,4,5,6)
    tuple2=('a','b','c','d','e','f')
    tuple3=("apple","bannana","orange")

    return tuple1,tuple2,tuple3

def access_tuples(tuple1, tuple2):
    print("Tuple 1: ", tuple1)
    print("First element of tuple1:",tuple1[0])
    print("Last element of tuple1:",tuple1[-1])
    print("Tuple 2: ", tuple2)
    print("Second element of tuple2:",tuple2[1])
    print("Second last element of tuple2:",tuple2[-2])
    print(tuple[0:5])

def unpacking_tuple(tuple3):
    (green,yellow,red)=tuple3
    print(green)
    print(yellow)
    print(red)

def unpacking_tuple2(fruits):
    fruits=("apple","bannana","cherry","strawberry","raspberry")
    (green,yellow,*red)=fruits
    print(green)
    print(yellow)
    print(red)

def change_tuples(tuple1, tuple2):
    list1=list(tuple1)
    list2=list(tuple2)
    list1.append(6)
    list2.remove('c')
    tuple1= tuple(list1)
    tuple2= tuple(list2)
    return tuple1, tuple2

def loop_through_tuple(tuple1):
    print("Looping through tuple1 using for loop:")
    for item in tuple1:
        print(item)

    print("\nLooping using while loop and index numbers:")
    index=0
    while index<len(tuple1):
        print(tuple[index])
        index+=1

def join_tuple(tuple1, tuple2):
    tuple3=tuple1 + tuple2
    return tuple3


tuple1, tuple2, tuple3=create_tuples()
access_tuples(tuple1, tuple2)
print()

unpacking_tuple(tuple3)
print()

fruits=("apple","bannnana","cherry","strawberry","raspberry")
unpacking_tuple2(fruits)
print()

tuple1, tuple2=create_tuples(tuple1, tuple2)
print("After making changes:")
access_tuples(tuple1, tuple2)
print()

tuple3 = join_tuple(tuple1,tuple2)
print("Joined tuple:", tuple3)
