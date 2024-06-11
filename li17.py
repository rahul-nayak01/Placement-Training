#write a pgm to partition a list around a given value such that all elements less than the given value come before it and all elements greater than the given value come after it.

def partition(lst, pivot):
    less_than= [x for x in lst if x < pivot]
    equal_to= [x for x in lst if x == pivot]
    greater_than= [x for x in lst if x > pivot]
    return less_than + equal_to + greater_than

my_list= [1,3,4,1,5,9,2,6,5]
pivot_value= 4
print("Partitioned list:", partition(my_list, pivot_value))