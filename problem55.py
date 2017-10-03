# https://projecteuler.net/problem=55

from utilities import *

numLychrel = 0;
for i in range(0, 10000):

    n = 0
    while not isPalindrome(i + int(str(i)[::-1]) ) and n<50:
        i = i + int(str(i)[::-1])
        n += 1
    # Didn't find a palindrome before n=50
    if n==50:
        numLychrel += 1

print(numLychrel)
