#N^p recrsive using stack   - time complexity-O(P) times  ex- 2**644=O(6)
"""
stack-
pow(2,5)
pow(2,4)
pow(2,3)
pow(2,2)
pow(2,1)
pow(2,0)

"""
"""
def power(N,P):
    if P==0:
        return 1
    return (N*power(N,P-1))

N=5
P=2

print(power(N,P))
"""
#recursive tree and 2^6=O(6)so time complexity=O(logP) base 2
#this is 
"""
def power(N,P):
    if P==1:
        return N
    temp=power(N,P//2)
    return temp*temp

N=2
P=64
print(power(N,P))
"""
#odd power

def power(N,P):
    if P==1:
        return N
    temp=power(N,P//2)
    if P%2!=0:
        return N*temp*temp
    else:
        return temp*temp

N=2
P=64
print(power(N,P))
