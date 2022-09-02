"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import math


n = int(input())    # n = 20

#   lcm(n1, n2, n3) = lcm(n1,lcm(n2, n3))
lcm = 1
for i in range(2, n+1):
    lcm = math.lcm(lcm, i)
print(lcm)

#   Answer = 232792560
