"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d = 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d = 1,000,000?
"""

import math

def isPrime(n):
    if((1 >= n)or(0 == n % 2)):
        return False
    else:
        l = int(n**0.5)
        i = 3
        r = n
        while((i <= l)and(0 != r)):
            r = int(n % i)
            i = i + 2
            while(not(isPrime(i))):
                i = i + 2
        return(0 != r)

def isPrime0(n):
    if(1 >= n):
        return False
    else:
        l = lessPrime(int(n**0.5))
        i = 0
        r = n
        while((i < len(l))and(0 != r)):
            r = int(n % l[i])
            i = i + 1
        return(0 != r)

def isPrime1(n):
    l = [0, 0]
    if (n<2):
        return None
    
    for i in range(2, n+1):
        l.append(i)
    i = 1
    while (i < len(l)-1)and (not(0 == l[-1])):
        i = i + 1
        t = i
        if 0 != l[i]:
            while (i*t < len(l)):
                if 0 != l[i*t]:
                    l[i*t] = 0
                t = t + 1

    return (0 != l[-1])

def isPrime2(n):
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

def gcd(m, n):
    if(m > n):
        return gcd(n, m)
    if(0 == m):
        return n
    return gcd(n % m, m)

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

def insertC2S(s, c, i):
    if(0 == i):
        return(c + s)
    elif(len(s) <= i):
        return(s + c)
    else:
        return(s[:i]+c+s[i:])

def permute(l):
    if(0 == len(l)):
        return []
    else:
        res = []
        tl = []
        c = l.pop()
        tl.append(c)
        while(0 < len(l)):
            ttl = []
            c = l.pop()
            while(0 < len(tl)):
                x = tl.pop()
                for i in range(0, len(x)+1):
                    ttl.append(insertC2S(x, c, i))
            for x in ttl:
                tl.append(x)
            if(0 == len(l)):
                res = tl
        return res

def select(x, l):
    if(0 == x):
        return []
    res = []
    if(1 == x):
        tl = []
        for i in l:
            tl.append(i)
            res.append([]+tl)
            tl = []
    else:
        for i in range(len(l)):
            tl = l[i+1:]
            for j in select(x-1, tl):
                res.append(j+[l[i]])
    return res

def isPer(m, n):
    lm = list(str(m))
    ln = list(str(n))
    if(len(lm) == len(ln)):
        lm.sort()
        ln.sort()
        return (lm == ln)
    else:
        return (len(lm) == len(ln))

def maxPrimeFactor(n, l):
    i = 0
    while((i < len(l))and(l[i] <= n)):
        i = i + 1
    pl = l[:i]
    i = len(pl)-1
    p = pl[i]
    while((0 < i)and(0 != n%p)):
        i = i - 1
        p = pl[i]
    return p

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
                return [i] + intoPrime(int(n/i))
    return [n]

def hasNoCommon(l1, l2):
    if (len(l1) > len(l2)):
        return hasNoCommon(l2, l1)
    else:
        i = 0
        while((i < len(l1))and(not(l1[i] in l2))):
           i = i + 1
        return len(l1) > i

def primize(lp, n):
    if(n in lp):
        return [n]
    else:
        half = math.floor(n/2)
        l = []
        i = 0
        while((i < len(lp))and(lp[i] < n)):
            if (0 == n % lp[i]):
                l.append(lp[i])
            i = i + 1
        return l


def primeRate(nlp, n):
    d = {}
    for i in nlp:
        d[i] = 0
    for np in nlp:
        r = 0
        t = n
        while(0 == t % np):
            r = r + 1
            t = int(t/np)
        d[np] = r
    return d

def rate(lp, n):
    nlp = primize(lp, n)
    up = 1
    down = 1
    for np in nlp:
        up = up * np
        down = down * (np - 1)
    return up / down

def allPrimes(lp, n, d):
    if(n in lp):
        d[n] = [n]
    else:
        i = 0
        tl = []
        while(0 != n % lp[i]):
            i = i + 1
        tl.append(lp[i])
        for j in d[n//lp[i]]:
            if(not(j in tl)):
                tl.append(j)
        d[n] = tl + []
    return d[n]
        
def dupSelect(x, l):
    res = []
    if(1 == x):
        for i in l:
            res.append([i])
    elif(x > 0):
        for i in l:
            for j in dupSelect(x-1, l):
                j.append(i)
                res.append(j + [])
    return res

N = 1000000
#N = 12
lp = lessPrime(N)
print(len(lp))
pls = []
ls = []
tot = N - 1
d = {}

for i in range(2, N):
    if(i%1000==0):
        print(i)
    if(i in lp):
        tot = tot + N - ((N-i)//i)
    else:
        nlp = primize(lp, i)
        t = 0
        for j in range(1, 1+len(nlp)):
            fss = select(j, nlp)
            for fs in fss:
                p = 1
                for f in fs:
                    p = p * f
                t = t + ((-1)**j)*((N-i)//p)
        tot = tot + N + t
    tot = tot - i
print(tot)
