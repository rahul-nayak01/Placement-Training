# Given an array of n numbers and another number x the task is to check whether or not there exist 2 element in the array whose exact sum is x.
#factorial time complex-O(n**2) n-lenght
def check_sum(arr,x):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==x):
                return True

    return False


arr=[1,2,3,4,5,6]   
x=5
print(check_sum(arr,x))

#or

def check_sum(arr, x):
    arr.sort()  # Sort the array in ascending order
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            return True
        elif current_sum < x:
            left += 1
        else:
            right -= 1

    return False

# Example usage
arr = [1, 4, 5, 2, 3, 6]
x = 5
print(check_sum(arr, x))  # Output: True