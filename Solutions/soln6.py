""""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


n = int(input()) # n = 100
sumn = int(n*(n+1)/2)
sqsum = 0
for i in range(1, n+1):
    sqsum = sqsum + i*i
print(sumn*sumn - sqsum)


# Answer = 25164150
