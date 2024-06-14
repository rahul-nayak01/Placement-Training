#Quick sort

def quick_sort(arr,low,high):
    if len(arr) <=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x <pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

arr=[3,5,2,5,7,2]
print(arr)

result=quick_sort(arr)
print(result)