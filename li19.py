#find the largest sub array sum of a given list.

def max_sub_array_sum(nums):
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

# Example usage:
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sub_array_sum(nums))  # Output: 7

#or

def max_sub_array_sum(l):
    curr_sum=max_sum= l[0]
    for i in l[1:]:
        curr_sum = max(i,curr_sum+i)
        max_sum= max(curr_sum,max_sum)
    return max_sum

list = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Max sum is:",max_sub_array_sum(list)) # Output: