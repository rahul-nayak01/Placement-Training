#find min and max element in list of elements without min and max built in function.

    
# Find min and max element in list of elements without min and max built-in function.

li = [23, 44, 66, 22, 78]

min_val = li[0]
max_val = li[0]

for i in li:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print("Minimum number:", min_val)
print("Maximum number:", max_val)