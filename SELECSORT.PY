#selection sort

def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if (arr[j] < arr[min_idx]):
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[min_idx]
arr=[34,56,34,79,78,89,90,95,23,12]
selection_sort(arr)
for i in range(len(arr)):
    print(arr[i])

#sel sor repeteadly finds min ele from the unsorted part and swaps with first unsorted element Time complexity O(n^2)

