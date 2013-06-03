"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

import math

def sep(m, n, mv):
    res = 0
    if((m < n)or(2 > n)):
        return 0
    elif(2 == n):
        return math.floor(m/2) - (m-1-mv)*(int(m-1-mv>0))
    elif(m-1 <= n):
        return 1
    else:
        res = 0
        for i in range(math.ceil(m/n), min(mv, m-n+1)+1):
            res = res + sep(m-i, n-1, i)# - sep(m-i, n-1, mv-i)*int(i <= mv)
        return res

def nos(n):
    res = 0
    for i in range(2, n+1):
        print(i)
        res = res + sep(n, i, n-i+1)
    return res

d = {}
print(nos(100))


def setup(m, d):
    d[m] = [m-1 + 0.01]
    for i in range(1, m-1):
        if(i >= math.ceil(m/2)):
            d[m].append(i + 0.01*(m-i))
        for j in d[m-i]:
            if(j < i+1):
                d[m].append(i+0.01*j)

N = 100
d = {1:[]}

for i in range(2, N+1):
    print(i)
    setup(i, d)
print(len(d[N]))
