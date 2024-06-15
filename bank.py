#u r given an m*n integer grid accounts where acc of [i,j] is amt of money the ith customer has in jth bank the cust wealth is amt of money in all thier bank account the richest customer is the customer that has the max wealth.

"""

def richest_customer(arr):
    max_wealth=0
    for i in range(len(arr)):
        wealth=0
        for j in range(len(arr[i])):
            wealth+=arr[i][j]
        if wealth>max_wealth:
            max_wealth=wealth
    return max_wealth


arr=[[1,5],[4,6],[7,4],[8,4],[9,4],[10,6]]
"""
#or

def richest_customer(arr):
    max_sum=0
    for i in range(len(arr)):
        sum=0
        for j in range(len(arr[i])):
            sum+=arr[i][j]
        if sum>max_sum:
            max_sum=sum
    return max_sum

arr=[[1,5],[4,6],[7,4],[8,4],[9,4],[10,6]]
print(richest_customer(arr))