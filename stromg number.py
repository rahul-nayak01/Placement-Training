#write a code in python to check if number is strong number.

def is_strong_number(num):
    sum = 0
    temp = num
    while(num!= 0):
        f = 1
        i = 1
        r = num % 10
        while(i <= r):
            f = f * i
            i = i + 1
        sum = sum + f
        num = num // 10
    if (temp == sum):
        return f"{temp} is a strong number"
    else:
        return f"{temp} is not a strong number"

# Example usage
number = int(input("Enter a number: "))
print(is_strong_number(number))
