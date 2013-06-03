"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
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

N = 5000

d = {2:[], 3:[]}
i = 3
while(len(d[i]) < N):
    i = i + 1
    d[i] = []
    lp = lessPrime(i)
    while(0 < len(lp)):
        p = lp.pop()
        if(i - p > 1):
            tl = [p]
            if((i-p == p)or((i-p) in lp)):
                tl.append(i-p)
                d[i].append(tl)
            for l in d[i - p]:
                if(l[0] <= p):
                    d[i].append(tl + l)
        else:
            tl = []
print(i, len(d[i]))
