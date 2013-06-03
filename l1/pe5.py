"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
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

x = 20
lp = lessPrime(x)
times = {}
res = 1

for i in lp:
    times[i] = 0

for i in range(2, x+1):
    for j in lp:
        t = i
        c = 0
        while (0 == t % j):
            t = int(t/j)
            c = c + 1
        times[j] = max(times[j], c)

for i in lp:
    res = res * math.pow(i, times[i])

print (res)
