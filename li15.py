#pgm to demonstrate list intersection and union.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = list(set(list1) & set(list2))
list4 = list(set(list1) | set(list2))
print(list3)
print(list4)