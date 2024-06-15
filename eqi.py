#equlibrium index is index such that sum of ele at lower index is equal to sumof  index at higher indices ex- array[-7,1,2,-4,3,0] o/p is 3

def equilibriumPoint(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num

    return -1  # If no equilibrium point found

arr=[0,1,2,3,4,5,6,7]

print(equilibriumPoint(arr))

#or

def equilibrium_index(arr):
    n=len(arr)
    for i in range(n):
        lsum=sum(arr[:i])
        rsum=sum(arr[i+1:])
        if lsum==rsum:
            return i
    return -1 # If no equilibrium point found

arr=[-7,1,5,2,-4,3,0]
print(equilibrium_index(arr))

#u r given an m*n integer grid accounts where acc of [i,j] is amt of money the ith customer has in jth bank the cust wealth is amt of money in all thier bank account the richest customer is the customer that has the max wealth.