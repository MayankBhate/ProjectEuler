"""Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"""


n = 1000
k = 13
f = open('problem8_number.txt', 'r')
lines = f.readlines()
num = ''
for line in lines:
    num = num + line.strip('\n')
maxprod = 0
for i in range(0, n-k+1):
    prod = 1
    for j in range(i, i+k):
        prod = prod*int(num[j])
    if prod >= maxprod:
        maxprod = prod
print(maxprod)


# Answer = 23514624000