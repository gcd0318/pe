"""
In the following equation x, y, and n are positive integers.

1x+1y=1n
For n = 4 there are exactly three distinct solutions:

15+12016+11218+18=14=14=14
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
"""


import math

def lessPrime(n):
    res = []
    l = [0,0]
    for i in range(2, n+1):
        l.append(i)
    for i in l:
        t = i
        while ((0 != l[i]) and (t+i < len(l))):
            t = t + i
            l[t] = 0
    for i in l:
        if(0 != i):
            res.append(i)
    return res

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
    while((0 < len(l)) and ((0 == i) or (0 != n % i))):
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
        while(0 == t % i):
            r = r + 1
            t = t // i
        d[i] = r
    return d

def top_n_primes(n):
    primes = []
    if (0 < n):
        ins = 2
        primes = [2]
        while(len(primes) < n):
            ins = ins + 1
            devided = False
            i = 0
            while not(devided) and (i < len(primes)):
                devided = (0 == ins % primes[i])
                i = i + 1
            if not devided:
                primes.append(ins)
    return primes

def nth_prime(n):
    res = 0
    if (0 < n):
        res = top_n_primes(n)[-1]
    return res

def mul(l):
    res = 1
    for i in l:
        res = res * i
    return res

def isPrime(n):
    l = [0,0]
    if(2 > n):
        return None
    else:
        for i in range(2, n+1):
            l.append(i)
        for i in l:
            t = i
            if(0 != l[i]):
                t = t + i
                while(t < len(l)):
                    l[t] = 0
                    t = t + i
    return(0 != l[n])

def sols(n):
    res = 1
    for i in prime_rate(n**2).values():
        res = res * (i+1)
    return math.ceil(res/2)

n = 2
s = sols(n)
m = s
while s < 1000:
    n = n + 1
    s = sols(n)
    if m < s:
        m = s
        print(m, n)
print(n)