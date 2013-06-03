"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =  n!
r!(nr)! ,where r  n, n! = n(n1)...321, and 0! = 1. 

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""

import math

def C(n, m):
    return int(math.factorial(n)/math.factorial(n-m)/math.factorial(m))

N = 1000000
tot = 0
for n in range(1, 100+1):
    r = -1
    c = 0
    while(N > c)and(r <= int(n/2)):
        r = r + 1
        c = C(n, r)
    if(N < c):
        tot = tot + (n-2*r+1)
print(tot)
