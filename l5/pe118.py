"""
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""

import math

def lessPrime(n):
    res = []
    l = [0,0]
    for i in range(2, n+1):
        l.append(i)
    m = len(l)//2 + 1
    i = 2
    while(i <= m):
        while (0 != l[i]):
            t = i * 2
            while (t < len(l)):
                l[t] = 0
                t = t + i
            i = i + 1
        i = i + 1
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

def betweenPrimes(s, e):
    resl = []
    for i in lessPrime(e):
        if i >=s:
            resl.append(i)
    return resl

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

sps = lessPrime(math.ceil(math.sqrt(98765431)))

def is_p(n):
    pivot = 0
    i = 0
    if (n in sps):
        i = len(sps)
    elif (n <= 98765431):
        pivot = math.sqrt(n)
        while (i < len(sps)) and (sps[i] <= pivot) and (0 == n % sps[i]):
            i = i + 1
    return (i >= len(sps)) or (sps[i] > pivot)

resl = []
for i in permute(list('123456789')):
    tmp = []
    if not(i[-1] in '468') and (not((i[-1] in '25') and (i[-2] in '468'))):
        h = 0
        t = len(i)
        s = h
        e = s + 1
        tmp = []
        if '2' == i[-1]:
            tmp = ['2']
            i = i[:-1]
        if i[0] in '14689':
            e = e + 1
        if (e > 1) and (i[e-1] in '1245689'):
            e = e + 1
        while (s < t-1) and (e <= t-1):
#            print(i, s, e)
            n = int(i[s: e])
            if is_p(n):
#                print(i, n)
                tmp.append(str(n))
                s = e
                e = s + 1
            else:
#                print(i, n, s, e)
                e = e + 1
#    print(tmp)
    if 9 == len(''.join(tmp)):
        tmp.sort()
#        print(tmp)
        t_s = '.'.join(tmp)
        if not (t_s in resl):
            resl.append(t_s)
#            print(t_s)
print(len(resl))
