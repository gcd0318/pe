"""
Consider quadratic Diophantine equations of the form:

x^(2) – Dy^(2) = 1

For example, when D=13, the minimal solution in x is 649^(2) – 13×180^(2) = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^(2) – 2×2^(2) = 1
2^(2) – 3×1^(2) = 1
9^(2) – 5×4^(2) = 1
5^(2) – 6×2^(2) = 1
8^(2) – 7×3^(2) = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

import math

def gcd(m, n):
    if(m > n):
        return(gcd(n, m))
    if(0 == m):
        return n
    return(gcd(n%m, m))

def cf(f):
    res = []
    his = []
    head = f
    foot = f.pop()
    x = head[0]
    r = head[1]
    
    rtx = int(math.sqrt(x))
    if(rtx**2 == x):
        if(x != 0):
            r = rtx
            x = 0
        d = r // foot
        res.append(d)
        r = r % foot
        tmp = foot
        foot = r
        r = tmp
        while(foot > 0):
            res.append(r // foot)
            r = r % foot
            tmp = foot
            foot = r
            r = tmp
        res.append(0)
    else:
        h = rtx + r
        t = h // foot
        d = t
        res.append(d)
        while(not([r, foot] in his)):
            his.append([r, foot])
            r = r - t * foot
            tmp = foot
            foot = x - r**2
            g = gcd(tmp, foot)
            if(g != 1):
                tmp = tmp // g
                foot = foot // g
            r = -r * tmp
            h = rtx + r
            t = h // foot
            res.append(t)
        if(res[his.index([r, foot])] == res[-1]):
            res.pop()
        res.append(his.index([r, foot]))
    return res


def isSquare(n):
    return((n >= 0)and((int(math.sqrt(n)))**2 == n))

def conv(n, d):
    a = cf([d, 0, 1])
    h = a.pop()
    if(0 == n):
        return ([a[0], 1])
    if(1 == n):
        return ([a[1]*conv(0, d)[0]+1, a[1]])
    return([a[n%(len(a)-1)+h-1]*conv(n-1, d)[0]+conv(n-2, d)[0],\
            a[n%(len(a)-1)+h-1]*conv(n-1, d)[1]+conv(n-2, d)[1]])


md = 0
mx = 0

for D in range(1000+1):
    if(not(isSquare(D))):
        x = 0
        y = 0
        i = 0
        a = cf([D, 0, 1])
        h = a.pop()
        convd = {0:[a[0], 1], 1:[a[1]*a[0]+1, a[1]]}
        while(x*x - D*y*y != 1):
            i = i + 1
            if(i in convd.keys()):
                [x, y] = convd[i]
            else:
                if(i >= len(a)):
                    im = 1+(i-1)%(len(a)-h)
                else:
                    im = i
                convd[i] = [a[im]*convd[i-1][0]+convd[i-2][0], a[im]*convd[i-1][1]+convd[i-2][1]]
            [x, y] = convd[i]
        if(x > mx):
            md = D
            mx = x
print(md)
