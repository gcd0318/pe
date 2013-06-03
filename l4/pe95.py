"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

import math

def sumOfDiv(n):
    res = set()
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if((0 == n % i)and(i != n)):
            res.add(i)
            if(1 != i):
                res.add(n // i)
    return sum(res)

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


N = 1000000
el = lessPrime(N)

d = {}
for e in el:
    d[e] = 1
for i in range(2, N+1):
    if(not(i in el)):
        sod = sumOfDiv(i)
        if(not((sod > N)or(sod in el)or(sod == i))):
            d[i] = sod

s = 0
while(len(d) != s):
    s = len(d)
    td = {}
    for k in d:
        if((d[k] in d)and(k in d.values())):
            td[k] = d[k]
    d = td.copy()

tl = []
s = 0
m = max(d.values())
i = 0
while(i < len(d)):
    k = list(d.keys())[i]
    while(not(d[k] in tl)):
        tl.append(d[k])
        k = d[k]
    td = {}
    for j in d:
        if(not(j in tl)):
            td[j] = d[j]
    d = td.copy()
    if((s < len(tl))or((len(tl) == s)and(m > min(tl)))):
        s = len(tl)
        m = min(tl)
    tl = []
print(m)
