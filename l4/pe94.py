"""


It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""

import math

def intoPrime(n):
    half = math.floor(math.sqrt(n))
    l = [0, 0]
    for i in range(2, half+1):
        l.append(i)
    i = 0
    while (i < len(l)):
        t = i
        if (0 != l[i]):
            while(t + i < len(l)):
                t = t + i
                l[t] = 0
        i = i + 1
    i = 0
    while((0 < len(l))and((0 == i)or(0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(n//i)
    return [n]

def prime_rate(x):
    l = intoPrime(x)
    d = {}
    for i in l:
        d[i] = 0
    for i in l:
        r = 0
        t = x
        while((0 == t % i)and(i != 1)):
            r = r + 1
            t = t // i
        d[i] = r
    return d

def isSq(x):
    d = prime_rate(x)
    res = (x % 10 in [0,1,4,5,6,9])
    kl = list(d.keys())
    i = 0
    while(res and(i < len(kl))):
        res = (0 == d[kl[i]] % 2)
        i = i + 1
    return res
            

def isASS(a, b, c):
    res = False
    s = a+b+c
    if(0 == s % 2):
        p = s // 2
        res = isS([p, p-a, p-b, p-c])
    return res

def isSS(a, b, c):
    if((a != b)or(0 != c%2)):
        return isASS(a, b, c)
    else:
        return isS([(a+c//2), (a-c//2)])

def isS(l):
    dl = []
    for x in l:
        dl.append(prime_rate(x))
    d = {}
    for dx in dl:
        for kx in dx:
            if(kx in d):
                d[kx] = d[kx] + dx[kx]
            else:
                d[kx] = dx[kx]
#    print(d)
    vl = list(d.values())
    i = 0
    v = vl[i]
    while((i < len(vl))and(0 == v % 2)):
        v = vl[i]
        i = i + 1
    return (i == len(vl))and(0 == v % 2)

def isSqr(n):
    r = math.ceil(math.sqrt(n))
    return r ** 2 == n

N = 1000000000
res = 0

for p in range(5, N+1):
    if(0 == p % 2):
        if(1 == p % 3):
            t2 = p * (p - 4) // 12
            x = (p-1) // 3
            if(1 == x % 2)and(isSqr(t2)):
                if(x**2 == t2 + ((x+1)//2)**2):
                    res = res + p
        elif(2 == p % 3):
            t2 = p * (p + 4) // 12
            x = (p+1) // 3
            if(1 == x % 2)and(isSqr(t2)):
                if(x**2 == t2 + ((x-1)//2)**2):
                    res = res + p
    p = p + 1
print(res)
