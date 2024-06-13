"""
O(1)=excellent
logn =goood
n=fair
nlogn=bad
n**2,2**n,n!=worst

cheat sheet for time complexity:

when your calc is not dependent on the input size,itis constant time 1
when ip size is reduced to half ,maybe when iteration,handling recursion, logn
when u hv a single loop within ur alogrithm=O(n)
when u hv nested loop within ur alogrithm,its quad O(n**2)
when a growth rate doubles with each addition to ip, its exponential time complexityO(2**n)

"""
#O(1)
def access_ele(arr,index):
    return arr[index]

arr=[1,2,3]
index=2
result=access_ele(arr,index)
print(f"element at index {index} is {result}")

#O(logn)
def peak_ele(arr,k):
    l=0
    r=len(arr)-1
    while(l<r):
        mid=l+(r-l)//2
        if mid==k:
            return mid
        elif mid>k:
            r=mid-1
        else:
            mid+1
    return -1

arr=[10,30,45,23,67,58,98]
key=45
result=peak_ele(arr,key)
if result!=-1:
    print(f"ele found at {result}")
else:
    print("no")


#O(n)
#recursive stack function

def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1

arr=[3,5,2,5,7,2]
target=5

result=linear_search(arr,target)

if result!=-1:
    print(f"Element found at {result}")
else:
    print("element not found")

#bubble sort

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[3,5,2,5,7,2]

result=bubble_sort(arr)

print(result)+-