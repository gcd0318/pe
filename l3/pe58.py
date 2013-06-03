"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

def isPrime(n):
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

def ur(n):
    return(7+2*n*(2*n-5))
def ul(n):
    return(5+4*n*(n-2))
def dl(n):
    return(3+2*n*(2*n-3))

import math
n = 10000
pl = lessPrime(n)
l = len(pl)
while(len(pl) >= n/10):
   n = n + 10000
   pl = lessPrime(n)
w = int(math.sqrt(n))-int(0==int(math.sqrt(n))%2)

d = 2*w-1
n = 0
pl = lessPrime(w*w)
dps = set([])
for i in range(1, int((w+1)/2)+1):
    if(0 != i % 7):
        x = ur(i)
        if(x in pl):
            dps.add(x)
    if(0 != i % 3):
        y = dl(i)
        if(y in pl):
            dps.add(y)
    if(0 != i % 5):
        z = ul(i)
        if(z in pl):
            dps.add(z)
n = len(dps)

while(n >= d/10):
    w = w + 2
#    bp = betweenPrime(5+w*(w-4), w*w)
    d = d + 4
    i = int((w+1)/2)
    if(0 != i % 7):
        x = ur(i)
        if(isPrime(x)):
#        if(x in bp):
#            dps.add(x)
            n = n + 1
    if(0 != i % 3):
        y = dl(i)
#        if(y in bp):
        if(isPrime(y)):
            n = n + 1
#            dps.add(y)
    if(0 != i % 5):
        z = ul(i)
        if(isPrime(z)):
            n = n + 1
#        if(z in bp):
#            dps.add(z)
#    n = len(dps)
    print(w, n, d)
print(w)
