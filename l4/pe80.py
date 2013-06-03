"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

import math

N = 100
sl = []
for i in range(math.floor(math.sqrt(N+1))+1):
    sl.append(i**2)
l = []
for i in range(1, N+1):
    if not(i in sl):
        l.append(i)

from decimal import *
getcontext().prec = 102
print(len(str(Decimal(2) ** Decimal('0.5'))[2:]))
print(len(l))
res = 0
for i in l:
    s = str(Decimal(i) ** Decimal('0.5')).replace('.', '')[:100]
    for c in s:
        res = res + int(c)
print(res)
