"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

def prod(l1, l2):
    res = -1
    if(len(l1) == len(l2)):
        res = 0
        for i in range(len(l1)):
            res = res + int(l1[i]) * int(l2[i])
    return res

def toIndex(n, l):
    res = ''
    if(n in range(2**l)):
        res = bin(n)[2:]
        while(len(res) < l):
            res = '0' + res
    return res

def findSum(s, ol, il):
    res = []
    for o in ol:
        for i in il:
            if(o + i == s):
                if(not([o, i] in res)):
                    res.append([o, i])
    return res

def unilist(l):
    res = 0
    for x in l:
        if(10 == x):
            res = res * 100 + x
        else:
            res = res*10 + x
    return res

def fillline(ld, s, e, il, ol, lsum, N):
    resl = []
    resd = {}
    for x in range(s, e+1):
        resd[x] = ld[x]
    noz = 0
    zl = []
    for i in resd.keys():
        if(0 == resd[i]):
            noz = noz + 1
            zl.append(i)
    if(2 != noz):
        if(1 == noz):
            zp = zl.pop()
            resd[zp] = lsum - sum(resd.values())
        resl = [resd]
    else:
        if((0 == zl[0]%N)or(0 == zl[1]%N)):
            grp = findSum(lsum - sum(resd.values()), ol, il)
        else:
            grp = findSum(lsum - sum(resd.values()), il, il)
        for g in grp:
            if(g[0] != g[1]):
                td = resd.copy()
                if(0 == zl[0] % N):
                    td[zl[0]] = g[0]
                    td[zl[1]] = g[1]
                else:
                    td[zl[0]] = g[1]
                    td[zl[1]] = g[0]
                resl.append(td)
    return resl

def spread(d, N):
    resd = d.copy()
    for x in range(N):
        i = N * x
        if((0 != resd[i+1])and(0 == resd[(i+1+N+1)%(N**2)])and(0 != (i+1+N+1)%N)):
            resd[(i+1+N+1)%(N**2)] = resd[i+1]
        if((0 != resd[i+2])and(0 == resd[(i+2-N-1)%(N**2)])and(0 != (i+2-N-1)%N)):
            resd[(i+2-N-1)%(N**2)] = resd[i+2]
    return resd

def oklist(l):
    ok = True
    s = sum(l[0:3])
    i = 0
    while(ok and(i < len(l))):
        ok = (s == sum(l[i:i+3]))
        i = i + 3
    return ok

def cycle(l, step):
    res = []
    for i in range(len(l)):
        res.append(l[(i+step)%len(l)])
    return res

def rev(l, p):
    res = []
    for i in range(len(l)//p):
        tl = []
        for j in range(p):
            t = l.pop()
            tl.append(t)
        tl.reverse()
        res = res + tl
    return res

N = 5
s = sum(range(2*N+1))
l1 = []
l2 = []
for i in range(0, N):
    l1.append(i+1)
    l2.append(2*N-i)
td = {}
sd = {}

for x in range(2**N):
    td[toIndex(x, N)] = \
      s + prod(l1, list(toIndex(x, N))) + prod(l2, list(toIndex(2**N-1-x, N)))
for i in td.keys():
    if((0 == td[i] % N)and('1' == i[0])):
        sd[i] = td[i]
kl = list(sd.keys())
kl.sort()

finallist = []

for k in kl:
    resl = []
    resd = {}
    for i in range(N):
        for j in range(3):
            resd[i*N+j] = 0
    linesum = sd[k] // N
    il = []
    ol = []
    d = {}
    for i in range(2*N):
        d[i+1] = 1
    for t in range(len(k)):
        it = int(k[t])
        if(1 == it):
            il.append(l1[t])
            ol.append(2*N+1-l1[t])
            d[l1[t]] = 2
        else:
            il.append(2*N+1-l1[t])
            ol.append(l1[t])
            d[2*N+1-l1[t]] = 2
    resd = {}
    for i in range(N):
        for j in range(3):
            resd[i*N+j] = 0
    begin = min(ol)
    resd[0] = begin    
    ol.remove(begin)
    resl.append(resd)

    while(0 < len(resl)):
        lil = []
        lol = []
        curd = resl.pop()
        if(not(0 in list(curd.values()))):
            l = list(curd.values())
            if(oklist(l)):
               finallist.append(l)
        else:
            for x in il:
                if(not(x in list(curd.values()))):
                    lil.append(x)
            for x in ol:
                if(not(x in list(curd.values()))):
                    lol.append(x)
            i = 0
            while((0 != curd[i]*curd[i+1]*curd[i+2])and(i < max(list(curd.keys())))):
                i = i + N
            if(0 != len(lol)*len(lil)):
                bllist = fillline(curd, i, i+2, lil, lol, linesum, N)
                if(0 < len(bllist)):
                    for bl in bllist:
                        d = curd.copy()
                        for j in range(i, i+3):
                            d[j] = bl[j]
                        d = spread(d, N)
                        resl.append(d)
            else:
                if(0 != len(lol)):
                    o = lol.pop()
                    curd[i] = o
                    curd[i+1] = curd[2]
                resl.append(curd)

print(finallist)
nl = []
for l in finallist:
    hl = []
    l = rev(l, 3)
    for i in range(N):
        hl.append(l[3*i])
    while(l[0] != min(hl)):
        l = cycle(l, 3)
    nl.append(l)

ml = 0
for l in nl:
    if(ml < unilist(l)):
        ml = unilist(l)
print(ml)
