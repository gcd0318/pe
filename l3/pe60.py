"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from collections import deque


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

def betweenPrime(m, n):
    if(m == n):
        return []
    elif(m < n):
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
            if((0 != i)and(i > m)):
                res.append(i)
        return res
    else:
        return(betweenPrime(n, m))

def insertC2S(s, c, i):
    if(0 == i):
        return([c]+s)
    elif(len(s) <= i):
        return(s + [c])
    else:
        return(s[:i]+[c]+s[i:])

def permute(l):
    if(0 == len(l)):
        return []
    else:
        res = []
        tl = []
        s = [l.pop()]
        tl.append(s)
        while(0 < len(l)):
            ttl = []
            c = l.pop()
            while(0 < len(tl)):
                x = tl.pop()
                for i in range(0, len(x)+1):
                    ttl.append(insertC2S(x, c, i))
            tl = tl + ttl
            if(0 == len(l)):
                res = tl
        return res

def collect(l, m):
    res = []
    if((0 < m)and(m <= len(l))):
        if(1 == m):
            for i in l:
                res.append([i])
        else:
            res1 = collect(l[1:], m-1)
            res2 = collect(l[1:], m)
            for r in res1:
                r.append(l[0])
                res.append(r)
            for r in res2:
                res.append(r)
    return res

def per(l, m):
    if(len(l) == m):
        return(permute(l))
    elif(len(l) < m):
        return []
    else:
        tl = collect(l, m)
        res = []
        for ln in tl:
            l = permute(ln)
            res = res + l
        return res

def nextPrimeList(n):
    k = int(n**0.5) + 1
    pl = betweenPrime(n, k**2)
    while(0 == len(pl)):
        k = k + 1
        pl = betweenPrime(n, k**2)
    return pl

def maxLen(d, p):
    if(not(p in list(d.keys()))):
        return 0
    elif(0 == len(d[p])):
        return 1
    else:
        m = 0
        t = 0
        for i in d[p]:
            for j in d[i]:
                if(j in d[p]):
                    t = 1 + maxLen(d, i)
            if(m < t):
                m = t
        return m

def connNo(a, b):
    return(int(str(a)+str(b)))

def joinable(l, p):
    i = 0
    res = True
    while((i < len(l))and res):
        res = isPrime(connNo(p, l[i])) and isPrime(connNo(l[i], p))
        i = i + 1
    return res

def col(l1, l2):
    resl = []
    for i in l1:
        if(i in l2):
            resl.append(i)
    return resl

def isPair(d, i, j):
    return((i in d[j])and(j in d[i]))

def cut(d, t):
    resd = d.copy()
    tocut = []
    kl = list(resd.keys())
    tmpd = {}
    for i in kl:
        if(len(resd[i]) < t):
            tocut.append(i)
    while(0 < len(tocut)):
        for i in kl:
            if(not(i in tocut)):
                tmpl = []
                for j in resd[i]:
                    if(not(j in tocut)):
                        tmpl.append(j)
                tmpd[i] = tmpl
        resd = tmpd.copy()
        tocut = []
        kl = list(resd.keys())
        tmpd = {}
        for i in kl:
            if(len(resd[i]) < t):
                tocut.append(i)
    for i in resd:
#        resd[i].sort()
        tmpl = []
        for j in resd[i]:
            if(i < j):
                tmpl.append(j)
        resd[i]=tmpl
        resd[i].sort()
    return resd

def reduce(d):
    td = {}
    for k in list(d.keys()):
        tl = []
        for i in d[k]:
            if(i > k):
                tl.append(i)
            tl.sort()
            td[k] = tl
    return td

def commonP(l, d):
    res = []
    if(1 == len(l)):
        x = l[0]
        res = d[x]
    elif(1 < len(l)):
        i = 0
        res = d[l[i]]
        i = i + 1
        while(i < len(l)):
            tl = []
            for x in d[l[i]]:
                if(x in res):
                    tl.append(x)
            res = tl + []
            i = i + 1
    return deque(res)

def isConnected(x,y,d):
    if (x<=y):
        return (y in d[x])
    else:
        return isConnected(y,x,d)

def push(d,val):
    d[len(d)] = val
    return d
def pop(d):
    if (0<len(d)):
        return(d[len(d)-1])
    else:
        return nil
    
size = 5
pl = [3, 7]
p = 11
N = 10000
pd = {3:[7],7:[3]}
tosearch = []
lessP = lessPrime(N)
while(p < N):
    p = p + 2
    while(not(isPrime(p))):
        p = p + 2
    pd[p] = []
    for i in pl:
        if((isPrime(connNo(p, i)))and(isPrime(connNo(i, p)))):
            pd[i].append(p)
            pd[p].append(i)
    pl.append(p)
    if(p >= N):
        pl.sort(reverse=True)
        resd = cut(pd, size-1)
        
        head = []
        pstack = []
        liststack = []
        plist=[]
        while(len(head) < size):
            if((0 == len(plist))and(0 < len(pstack))):
                head = pstack.pop()
                plist = deque(liststack.pop())
            elif((0 == len(plist))and(0 == len(pstack))):
                if(0 < len(head)):
                    head.pop()
                head.append(pl.pop())
                plist = commonP(head, resd)
            while((0 < len(plist))and(len(head) < size)):
                pltop = plist.popleft()
                pstack.append([]+head)
                liststack.append([]+list(plist))
                head.append(pltop)
                plist = commonP(head, resd)

        if(size <= len(head)):
            print(head, sum(head))
        else:
            N = N + 5000
