#find the peak elemeent in list of integer .peak element is element that is greater than or equal to its neighbor element.
"""
def find_peak_element(nums):
    for i in range(len(nums)):
        if i == 0:
            if nums[i] >= nums[i+1]:
                return nums[i]
        elif i == len(nums) - 1:
            if nums[i] >= nums[i-1]:
                return nums[i]
        else:
            if nums[i] >= nums[i-1] and nums[i] >= nums[i+1]:
                return nums[i]
    return None  # If no peak element is found

# Example usage:
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 3
"""
#or

def find_peak_element(li):
    if not li:
        return None
    l , r= 0, len(li)-1
    while l<r:
        mid=l+(r-l)//2
        if li[mid]<li[mid+1]:
            l=mid+1
        else:
            r=mid
    return li[l]

list=[1,3,6,10,8,2,4]
print(find_peak_element(list)) # Output: