def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime_range(n):
    prime_numbers = []
    for num in range(1, n+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

n = 100
prime_numbers = check_prime_range(n)
print(prime_numbers)