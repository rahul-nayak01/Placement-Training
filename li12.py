#find out duplicate removal list product using list comprehension.
"""
my_list = [1, 2, 3, 2, 4, 5, 1]
unique_list = [x for n, x in enumerate(my_list) if x not in my_list[:n]]
product = 1
for num in unique_list:
    product *= num
print(product)  # Output: 120

#or 

li=[10,20,30,40,50,60,40,30,40,50,10,30]
unique=[]
count=0
for i in li:
    if i not in unique:
        unique.append(i)
        count += 1
print(unique) 

product = 1
for i in unique:
    product *= i
print(product)  # Output: 120
"""
#or

def product(res):
    product=1
    for i in res:
        product *= i
    return product

li=[1,2,6,3,2,6,7,1]
res=[]
[res.append(i) for i in li if i not in res]
print(product(res))
      