"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def d(n):
    res = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if(0 == n % i):
            res.append(i)
            if(1 != i):
                res.append(int(n/i))
    tot = 0
    for i in res:
        tot = tot + i
    return tot

def isAmicable(a, b):
    return ((d(a) == b)and(d(b) == a)and(a != b))

tot = 0
for i in range(1, 10000+1):
    if(isAmicable(i, d(i))):
        tot = tot + i + d(i)
tot = int(tot / 2)
print (tot)
