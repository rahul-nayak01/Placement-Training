#write a pgn to extract elements with  freq greater than k.
def extract_elements_with_freq_greater_than_k(lst, k):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    result = [num for num, count in freq.items() if count > k]
    return result

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 4, 4]
k = 2
result = extract_elements_with_freq_greater_than_k(my_list, k)
print(result)  # Output: [2, 4]

#or

li=[4,6,3,6,7,4,4,4,4,4,8,8,8,8,5]
k=2
res=[]
for i in li:
    freq=li.count(i)
    if freq>k and i not in res:
        res.append(i)
print(res)
