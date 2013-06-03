"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

import math

def length(d, n):
    if not(n in list(d.keys())):
        s = 0
        for i in list(str(n)):
            s = s + math.factorial(int(i))
        if (n != s):
            if not(s in list(d.keys())):
                d[s] = length(d, s)
            d[n] = d[s] + 1
        else:
            d[n] = 1
            spread(d, n)
    return d[n]

def spread(d, k):
    tl = list(str(k))
    rl = []
    r = 0
    for i in tl:
        if(i in ['0', '1']):
            r = r + 1
        else:
            rl.append(i)
    l = []
    for c in range(2**r):
        l = l + permute(rl + list(str(bin(c))[2:]))
    for x in l:
        if((len(x) == len(str(k)))and(x != k)):
            d[int(x)] = 2

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

def insertC2S(s, c, i):
    if(0 == i):
        return(c + s)
    elif(len(s) <= i):
        return(s + c)
    else:
        return(s[:i]+c+s[i:])

def trans(x):
    res = 0
    for x in list(str(x)):
        res = res + math.factorial(int(x))
    return res

N=1000000
#N = 10
d = {145:1, 169:3, 871:2, 872:2, 45362:2, 45361:2, 363601:3, 1454:3, 69:5, 78:4, 540:2}
spread(d, 145)
print(d)
t = 0
for i in range(N):
    if(i%10000==0):
        print(i, t, len(d))
    if(length(d, i) == 60):
        t = t + 1
        print(i)
print(t)
