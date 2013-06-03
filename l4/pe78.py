"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
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


N = 1000000

d = {1:[[1]], 2:[[1,1], [2]]}
n = 1
"""
while(len(d[n]) % N != 0):
    n = n + 1
    if(n % 10 == 0):
        print(n, len(d[n-1]))
    if not(n in d):
        d[n] = [[n]]
        for i in range(1, n):
            if not((n-i) in list(d.keys())):
                p(n-i, d)
            for l in d[n-i]:
                if(l[0] <= i):
                    tl = l + [i]
                    tl.sort(reverse = True)
                    d[n].append(tl)
print(n)
"""

def p(n, i, d):
    k = n*1000000+i
    if k in list(d.keys()):
        return d[k]
    elif(n == 0):
        d[k] = 0
        return 0
    elif (n < i):
        k = n*1000000+n
        d[k] = p(n,n,d)
        return d[k]
    elif(i == 1):
        return 1
    elif (n == i):
        res = 1
    else:
        res = 0
#    print(n, i, res, 'pre')
    for j in range(1, i+1):
        res = res + p(n-j, min(i, j), d)
#    print(n, i, res)
    d[k] = res
    return res

N = 1000000

d = {}
n = 5
"""
while(res % N != 0):
    n = n + 1
    res = p(n,n, d)
    if(n % 10 == 0):
        print(n, res)
print(n)
"""

def sep(n, p, m, d):
#    print(n, p, d)
    for j in range(1, n+1):
        d[j*1000000+1] = 1
        d[j*1000000+j] = 1
    k = n*1000000+p
    if k in list(d.keys()):
        return d[k]
    if((p > n)or(p*m < n)):
        return 0
    elif(p != 1):
        res = 0
        for j in range(math.ceil(n/p), m+1):
            if(k == 6000003):
                print(n, p, j, sep(n-j, p-1, j, d))
            res = res + sep(n-j, p-1, j, d)
        d[k] = res
    return d[k]

def f(n, d):
    res = 0
    for i in range(n):
#        print(i+1, sep(n, i+1, n, d))
        res = res + sep(n, i+1, n, d)
    return res



def p2(n, m, d):
    if(n < m):
        return p2(n, n, d)
    if not(n in list(d.keys())):
        d[n] = [0, 1]
        td={1:1, n:1, n-1:1}
        for i in range(2, n-1):
            td[i] = p2(n-i, i, d)
        for k in range(2, len(td)+1):
            d[n].append(td[k] + d[n][k-1])
    return d[n][m]


def p3(n):
    h = []
    t = []
    r = [0]
    for i in range(n+1):
        h.append(1)
    for i in range(1+n//2):
        t.append(1)
    for i in range(1, n):
        r = []
        for j in range(n+1):
            r.append(0)
#        print(i, len(h), len(t), len(r))
        for hi in range(n+1):
            ti = 0
            ri = hi + ti*(i+1)
            while(ti < len(t)):
#                print(hi, h, ti, t, ri, r)
                if(ri <= n):
                    r[ri] = r[ri] + t[ti]*h[hi]
                ti = ti + 1
                ri = hi + ti*(i+1)
#            print('r', r)
        h = []
        for ri in range(len(r)):
            if(ri <= n):
                h.append(r[ri])
        t = []
        for j in range(1+n//(i+2)):
            t.append(1)
    return r[n]


def p4(n, d):
    if(n in list(d.keys())):
        return d[n]
    elif(n < 0):
        return 0
    elif(n == 1):
        return 1
    else:
        k = 1
        n1 = n - (3*k*k-k)//2
        n2 = n - (3*k*k+k)//2
        res = 0
        while(0 <= n2):
            res = res + ((-1)**(k-1))*(p4(n1, d)+p4(n2, d))
            k = k + 1
            n1 = n - k*(3*k-1)//2
            n2 = n - k*(3*k+1)//2
        res = res + ((-1)**(k-1))*(p4(n1, d)+p4(n2, d))
        d[n] = res
        return res

d = {0:1}
i = 1
while(p4(i, d)%1000000 != 0):
    if(i % 10000 == 0):
        print(i)
    i = i + 1
print(i)
