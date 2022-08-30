"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import math


def isprime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for j in range(2, math.floor(math.sqrt(num))+1):
            if num % j == 0:
                return False
        return True


n = 1   # First prime is 2.
prime = 2
i = 3

while n != 10001:
    if isprime(i):
        prime = i
        n = n + 1
    i = i + 2
print(prime)

# Answer = 104743
