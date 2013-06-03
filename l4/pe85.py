"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""
import math

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

def c(n, m):
    return int(math.factorial(n)/math.factorial(n-m)/math.factorial(m))

def recs(x, y):
    res = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
            res = res + i*j
    return res

N = 2000000
d = {}

M = math.sqrt(N)

for x in range(1, math.floor(M)):
    for y in range(x, math.floor(N/x/(x+1))):
        d[10000*x+y] = abs(N - x*(x+1)*y*(y+1)/4)
m = min(d.values())
for k in d:
    if(d[k] == m):
        print((k//10000)*(k%10000))
