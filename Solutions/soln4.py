"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def ispalindrome(num):
    num = str(num)
    return num == num[::-1]


def is3digitfactor(num):
    for k in range(100, 1000):
        if num % k == 0 and len(str(int(num/k))) == 3:
            return True


n = 999*999     # Maximum product obtained from two 3 digit numbers.
for j in range(n - 1, 101100, -1):
    if ispalindrome(j) and is3digitfactor(j):
        print(j)
        break


#   Answer = 906609
