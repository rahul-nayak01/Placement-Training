#distance
"""
from collections import namedtuple
import math

Point = namedtuple('Point',['x', 'y',])

point1=Point(1,2)
point2=Point(3,4)

distance = math.sqrt((point2.x- point1.x)**2 + (point2.y- point1.y)**2)

print(distance)
"""
#filter
tuple=(1,2,3,4,5)
filtered_tuple= tuple(filter(lambda x: x%2==0,tuple))
print(filtered_tuple)
tuple=(1,2,3,4,5)
filtered_tuple= tuple(filter(lambda x: x%2==0,tuple))
print(filtered_tuple)

# reduce
#import reduce
#reduce(fn,t)

from functools import reduce

def add(x,y):
    return x+y

original_tuple = (1,2,3,4,5)

result= reduce(add, original_tuple)
print(result)