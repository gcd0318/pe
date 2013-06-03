"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
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
    
def phi(n):
    resl = []
    for i in range(n):
        if(1 == gcd(i, n)):
            resl.append(i)
    return len(resl)

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

def phi3(n):
    if(1 == n):
        return 1
    pl = lessPrime(n)
    tl = []
    res = n
    for p in pl:
        if(0 == n%p):
            tl.append(p)
    for i in range(1, len(tl)+1):
        l = select(i, tl)
        for x in l:
            prod = 1
            for s in x:
                prod = prod * s
            res = res + ((-1)**i) * (n//prod)
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

def phi5(lp, n):
    nlp = primize(lp, n)
    tl = list(range(n))
    for nl in nlp:
        j = nl
        while(j < n):
            if(tl[j] != 0):
                tl[j] = 0
            j = j + nl
    res = 0
    for l in tl:
        res = res + int(l != 0)
    return res

def phi6(lp, n):
    if(1 == n):
        return 1
    elif(n in lp):
        return n - 1
    else:
        nlp = primize(lp, n)
        no = 0
        for i in range(len(nlp)+1):
            for tl in select(i, nlp):
                d = n
                for div in tl:
                    d = d / div
                no = no - d * (-1)**i
        return n - no

def phi7(lp, n):
    if(1 == n):
        res = 1
    elif n in lp:
        res = n - 1
    else:
         res = 1
         d = primeRate(primize(lp, n), n)
         ps = list(d.keys())
         for p in ps:
             res = res * (p-1)*(p**(d[p]-1))
    return res

def rate(lp, n):
    nlp = primize(lp, n)
    up = 1
    down = 1
    for np in nlp:
        up = up * np
        down = down * (np - 1)
    return up / down

N = 10**7
lp = lessPrime(math.ceil(N/2))
top = max(primize(lp, 87109)+[math.ceil(N**0.5)])
print(top)
lpN = []
i = 0
mid = math.floor(N**0.5)
while(lp[i] < mid):
    lpN.append(lp[i])
    i = i + 1
while(i > 0):
    i = i - 1
    p = lpN[i]
    print(p)
    q = math.floor(N/p)
    while(q >= mid):
        while(not(q in lp)):
            q = q - 1
        if isPer(p*q, (p-1)*(q-1)):
            print(p*q)
        else:
            q = q - 1
