def is_prime(num):
    if num > 2 and num % 2 == 0  :
        return  False
    else:
        return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
# -------------------------
def prime(n):
    primes = []
    for i in range(n + 1):
        if i < 2:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

# Example usage
print(prime(11))  # Output: [2, 3, 5, 7, 11]
# --------------------------------------------

# Using module : sympy

from sympy import isprime, primerange

# Check if a number is prime
print(isprime(17))  # Output: True

# Get all prime numbers from 1 to 20
print(list(primerange(1, 21)))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
