""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. """


n = int(input())   # n = 1000
n3 = (n-1)//3
n5 = (n-1)//5
n15 = (n-1)//15
S3 = (3*(n3*(n3+1)))//2
S5 = (5*(n5*(n5+1)))//2
S15 = (15*(n15*(n15+1)))//2
print(int(S3+S5-S15))

# Answer = 233168
