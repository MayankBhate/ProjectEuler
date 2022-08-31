import math, time


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


n = int(input())        # n = 600851475143
factors = [1, n]
i = 2
while i*i <= n:
    if n % i == 0:
        factors.append(i)
        if i != n/i:
            factors.append(n/i)
    i = i + 1
factors.sort()
for j in range(len(factors)-1, 0, -1):
    if isprime(factors[j]):
        print(int(factors[j]))
        break

#   Answer = 6857
