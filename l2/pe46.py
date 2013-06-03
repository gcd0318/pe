"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

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

def isCG(n):
    res = False
    lp = lessPrime(n+1)
    while((0 < len(lp))and(not res)):
        i = lp.pop()
        r = math.sqrt((n-i)/2)
        res = res or(r == int(r))
    return res

def isCG2(n, pl):
    lp = list(pl)
    res = False
    while((0 < len(lp))and(not res)):
        i = lp.pop()
        r = math.sqrt((n-i)/2)
        res = res or(r == int(r))
    return res

i = 9
while(isCG(i)):
    i = i + 2
print(i)


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

i = 9
lp = lessPrime(i)
while(isCG2(i, lp)):
    i = i + 2
    while(isPrime(i)):
        lp.append(i)
        i = i + 2
print(i)
