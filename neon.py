def is_neon_number(num):
    sqr = num * num
    temp = num
    sum = 0

    while num!= 0:
        r = sqr % 10
        sum = sum + r
        sqr = sqr // 10

    if sum == temp:
        return f"{temp} is a neon number"
    else:
        return f"{temp} is not a neon number"

# Example usage
num = int(input("Enter a number: "))
print(is_neon_number(num))