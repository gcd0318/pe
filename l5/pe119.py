"""


The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
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
    if (2 <= n):
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

# sps = lessPrime(math.ceil(math.sqrt(98765431)))

def is_p(n):
    pivot = sps[-1]
    i = 0
    if (n in sps):
        i = len(sps) + 1
    elif (1 < n <= 98765431):
        pivot = math.sqrt(n)
        while (i < len(sps)) and (sps[i] <= pivot) and (0 != n % sps[i]):
            i = i + 1
    return (i >= len(sps)) or (sps[i] > pivot)


def layer(n):
    s = str(n)
    return (s[-1] in '468') or ((1 < len(s)) and (s[-1] in '25'))


def split_prime(n):
    res = {}
    if not(((n % 10) in (4, 6, 8)) or (((n % 10) in (2, 5)) and (((n // 10) % 10) in (4, 6, 8)))):
        s = str(n)
        sep = 1
        isp = False
        while (sep <= len(s)) and not isp:
            isp = isPrime(int(s[:sep]))
            if not isp:
                sep = sep + 1
        head = int(s[:sep])
        if (sep < len(s)):
            tails = split_prime(int(s[sep:]))
            if (0 < len(tails)):
                res = {head}.union(tails)
        elif isp:
            res = {head}
    return res

def rev_split_prime(n):
    res = {}
    if not(((n % 10) in (4, 6, 8)) or (((n % 10) in (2, 5)) and (((n // 10) % 10) in (4, 6, 8)))):
        s = str(n)
        sep = len(s) - 1
        isp = False
        tail = int(s[sep:])
        while (0 < sep) and not isp:
            print(sep)
            tail = int(s[sep:])
            isp = isPrime(tail)
            if not isp:
                sep = sep - 1
        print(sep, tail)
        if (0 < sep):
            heads = rev_split_prime(int(s[:sep]))
            if (0 < len(heads)):
                res = {tail}.union(heads)
        elif isp:
            res = {tail}
    return res

def is_prime(n):
    i = 3
    res = ((n < 10) and not (n in (2, 3, 5, 7))) or ((2 < n) and (0 == n % 2))
    while (not res) and (i * i <= n):
        res = (0 == n % i)
        i = i + 2
    return not res

def primes(m):
    ps = [2]
    for n in range(m + 1):
        res = (n <= 2)
        i = 0
        while (not res) and (ps[i] ** 2 <= n):
            res = (0 == n % ps[i])
            i = i + 1
        if not res:
            ps.append(n)
    return ps

def is_dps(i):
    s = sum(int(x) for x in str(i))
    m = s
    if (1 < m):
        while m < i:
            m = m * s
    return (10 <= i) and (m == i)


if __name__ == '__main__':
    T = 30

    l = []
    d = 1
    while len(l) <= T:
        d = d + 1
        for i in range(2, 10 * d):
            max_rates = math.floor(math.log(10 ** d, i))
            rates = math.ceil(math.log(10 ** (d - 1), i))
            ds = i ** rates
            while rates <= max_rates:
                if is_dps(ds) and (not(ds in l)):
                    print(d, 'digits, base', i, 'rate', rates, ds)
                    l.append(ds)
                rates = rates + 1
                ds = ds * i
    l.sort()
    print(len(l))
    print(l)
    for i in range(len(l)):
        print(i + 1, l[i])

