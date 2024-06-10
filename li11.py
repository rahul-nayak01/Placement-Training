#Wrie a pgm to count a unique value in the list.
"""def count_unique_values(lst):
    unique_values = set(lst)
    count = {value: lst.count(value) for value in unique_values}
    return count

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 4, 4]
result = count_unique_values(my_list)
print(result) 
#or

def count_unique_values(lst):
    unique_values = set(lst)
    count = {}
    for value in unique_values:
        count[value] = lst.count(value)
    return count

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 4, 4]
result = count_unique_values(my_list)
print(result)  # Output: {1: 2, 2: 2, 3: 1, 4: 3, 5: 1}
"""
#or

li=[10,20,30,40,50,60,40,30,40,50,10,30]
unique=[]
count=0
for i in li:
    if i not in unique:
        unique.append(i)
        count += 1
print(count)
print(unique) # Output:
