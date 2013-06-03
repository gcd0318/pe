"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

import math

def lessPrime(n):
    res = []
    l = [0,0]
    for i in range(2, n+1):
        l.append(i)
    for i in l:
        t = i
        while ((0 != l[i])and(t+i < len(l))):
            t = t + i
            l[t] = 0
    for i in l:
        if(0 != i):
            res.append(i)
    return res

def s(a, b, c):
    return a**2 + b**3 + c**4

N = 50000000
lps = lessPrime(math.ceil(math.sqrt(N)))

print(len(lps))

i = 0
nd = {}
while(i < len(lps)):
    a = lps[i]
    j = 0
    b = lps[j]
    while((j < len(lps))and(s(a, b, 2) < N)):
        b = lps[j]
        k = 0
        c = lps[k]
        n = s(a, b, c)
        while((k < len(lps))and(n < N)):
            c = lps[k]
            n = s(a, b, c)
            if(n < N):
                nd[n] = 0
            k = k + 1
        j = j + 1
    i = i + 1

print(len(nd))
