#given an array of size n-1 such that it only contain ditinct integer in range of 1 to n find the missing ele ,i/p n=10 and arr=[6,1,2,8,3,4,7,10,5].
n = 10
arr = [6, 1, 2, 8, 3, 4, 7, 10, 5]

# Calculate the sum of the first n natural numbers
total_sum = n * (n + 1) // 2

# Calculate the sum of the given array
arr_sum = sum(arr)

# Find the missing element by subtracting the sum of the array from the total sum
missing_element = total_sum - arr_sum

print(missing_element)