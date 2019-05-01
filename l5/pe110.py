"""
In the following equation x, y, and n are positive integers.

1
x
+   
1
y
=   
1
n
It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
"""


import math

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
    d = {}
    if(1 < x):
        l = intoPrime(x)
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

def find(n):
    res = 1
    ps = prime_rate(n)
    rs = []
    for k in ps:
        for i in range(ps[k]):
            rs.append(k)
    rs.sort(reverse=True)
    primes = top_n_primes(len(rs))
    i = 0
    while i < len(rs):
        res = res * (primes[i] ** (math.ceil((rs[i] - 1) / 2)))
        i = i + 1
    return res

def get_n(s):
    i = s
    v = math.floor(math.sqrt(i*2))
    while(0 == v % 2):
        i = i + 1
        v = math.floor(math.sqrt(i*2))
    return find(v**2)

def a_num(num):
    res = 1
    ps = lessPrime(num)
    i = 0
    while (i < len(ps)) and (res < num):
        res = res * ps[i]
    return res


def nod(n):
    return pr2nod(prime_rate(n))

def nextPrime(n):
    if isPrime(n):
        n = n + 1
    while not isPrime(n):
        n = n + 1
    return n

def max_p(num):
    p = 3
    i = 1
    while p < num:
        p = p * 3
        i = i + 1
    return top_n_primes(i+1)


def prod(l):
    res = 1
    for i in l:
        res = res * i
    return res

def pr2n(pr):
    res = 1
    for p in pr:
        res = res * (p**pr[p])
    return res

def pr2nod(pr):
    res = 1
    for v in pr.values():
        res = res * (v*2 + 1)
    return res

def permute_list(l):
    resl = [l]
    i = 0
    while (i < len(resl)):
        tmpl = resl[i]
        for j in range(len(tmpl)):
            rl = tmpl[:j] + tmpl[j+1:]
            if not(rl in resl):
                resl.append(rl)
        i = i + 1
    return resl

def addd(d1, d2):
    resd = d1.copy()
    for k2 in d2:
        if k2 in resd:
            resd[k2] = resd[k2] + d2[k2]
        else:
            resd[k2] = d2[k2]
    return resd

num = 4000000
ps = max_p(num)
print(ps)
pr  ={}
for p in ps:
    pr[p] = 1
ps.sort(reverse=True)
m = pr2n(pr)
mr = math.ceil(math.log2(m))
print(m, mr)
ms = []

for p in ps:
    i = 2
    tpr = pr.copy()
    while (i < p) and (pr2nod(tpr) >= num*2 - 1):
        pr = tpr.copy()
        while (tpr[p] > 0) and (pr2nod(tpr) >= num*2 - 1):
            tpr[p] = tpr[p] - 1
            tpr = addd(tpr, prime_rate(i))
        if pr2nod(tpr) < num*2 - 1:
            tpr = pr.copy()
        i = i + 1
print(pr2n(pr))