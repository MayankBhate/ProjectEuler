n = int(input().strip()) # n = 4*(10**6)
a = 1
b = 2
c = a + b
evensum = 2
while c <= n:
    a, b = b, c
    c = a + b
    if b % 2 == 0:
        evensum = evensum + b
print(evensum)
