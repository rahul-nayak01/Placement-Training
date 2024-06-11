my_tuple =(1,2,3)
another_tuple = tuple([4,5,6])
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
combined_tuple = my_tuple + another_tuple
print(combined_tuple)
repeated_tuple= my_tuple*3
print(repeated_tuple)
print(2 in my_tuple)
print(4 in my_tuple)
print(len(my_tuple))
for item in my_tuple:
    print(item)
string_to_tuple=tuple("hello")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(2))
print(my_tuple.index(3))

tuple_of_integers=(5,2,8,1,3)                      #t.sort() is defined
sorted_tuple = tuple(sorted(tuple_of_integers))
print("Sorted tuple:",sorted_tuple)

tuple_of_integers=((1,'appple'),(2,'orange'),(3,'bannana'))
sorted_tuple = tuple(sorted(tuple_of_integers,key=lambda x: x[1]))
print("Sorted tuple:",sorted_tuple)

#tuple comprehension

squares_tuple = tuple(x**2 for x in range(1,6))
print(squares_tuple)

#zip
l1=[1,2,3]
l2=['a','b','c']
zip=tuple(zip(l1,l2))
print(zip)