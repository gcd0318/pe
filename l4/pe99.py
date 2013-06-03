"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math

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

def primeRate(x):
    l = intoPrime(x)
    d = {}
    for i in l:
        d[i] = 0
    for i in l:
        r = 0
        t = x
        while(0 == t % i):
            r = r + 1
            t = int(t/i)
        d[i] = r
    return d

def comp(e1, e2):
    if(e1[0] == e2[0]):
        return e1[1] <= e2[1]
    elif(e1[1] == e2[1]):
        return e1[0] <= e2[1]
    elif((e1[0] <= e2[0])and(e1[1] <= e2[1])):
        return True
    elif((e1[0] > e2[0])and(e1[1] > e2[1])):
        return False
    else:
        d1 = primeRate(e1[0])
        d2 = primeRate(e2[0])
        for k1 in d1:
            d1[k1] = d1[k1] * e1[1]
        for k2 in d2:
            d2[k2] = d2[k2] * e2[1]
        print(d1, d2)
        return bool(-1)

print(comp((46631,643714), (492397,527958)))
