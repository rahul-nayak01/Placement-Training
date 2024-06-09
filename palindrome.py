def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)

    # Reverse the string
    reversed_str = num_str[::-1]

    # Check if the original string is equal to the reversed string
    if num_str == reversed_str:
        return True
    else:
        return False

# Example usage
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")