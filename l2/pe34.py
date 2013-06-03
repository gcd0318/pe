"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def isCur(n):
    tot = 0
    s = str(n)
    for i in s:
        tot = tot + math.factorial(int(i))
    return (tot == n)

res = 0
for i in range(3, 10**6):
    if(isCur(i)):
        res = res + i
        print(i)
print(res)
