"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import math

def isConn(x, y):
    lx = list(str(x))
    ly = list(str(y))
    lx.sort()
    ly.sort()
    return (lx == ly)

def insertC2S(s, c, i):
    if(0 == i):
        return([c]+s)
    elif(len(s) <= i):
        return(s + [c])
    else:
        return(s[:i]+[c]+s[i:])

def permute(l):
    if(0 == len(l)):
        return []
    else:
        res = []
        tl = []
        s = [l.pop()]
        tl.append(s)
        while(0 < len(l)):
            ttl = []
            c = l.pop()
            while(0 < len(tl)):
                x = tl.pop()
                for i in range(0, len(x)+1):
                    ttl.append(insertC2S(x, c, i))
            tl = tl + ttl
            if(0 == len(l)):
                res = tl
        return res

def is3r(x):
    r = round(math.pow(x, 1/3))
    i = int(r)
    return (i**3 == x)

def no3r(l, minimum):
    res = 0
    rl = []
    tl = []
    for i in l:
        x = int("".join(i))
        if((x >= minimum)and(not(x in tl))):
            tl.append(x)
    for x in tl:
        if(is3r(x)):
            res = res + 1
            rl.append(round(math.pow(x, 1/3)))
    return res, rl


'''
i = 5
no = 0
c = 0
rl = []

while(no < 5):
    if(not(i in rl)):
        tl = []
        c = i**3
        print(i)
        s = str(c)
        l = permute(list(s))
        no, tl = no3r(l, c)
        for x in tl:
            rl.append(x)
    i = i + 1

print(c, no, rl)
'''

h = 1
t = 9
n = 1
N = 5
while(n < N):
    rl = list(range(h, t+1))
    cl = []
    cd = {}
    for r in rl:
        cl.append(r**3)
    for c in cl:
        tl = list(str(c))
        tl.sort()
        cd[c] = tl
    kl = list(cd.keys())
    kl.sort()
    for i in range(0, len(cl)):
        conn = 1
        k1 = cl[i]
        l1 = cd[k1]
        s1 = "".join(l1)
        for j in range(i+1, len(cl)):
            k2 = cl[j]
            if((len(str(k1)) == len(str(k2)))and(k1 in kl)and(k2 in kl)):
                l2 = cd[k2]
                s2 = "".join(l2)
                if(s1 == s2):
                    conn = conn + 1
                    kl.remove(k2)
        if(conn > n):
            n = conn
            print(n, round(math.pow(k1, 1/3)), k1)
        if(k1 in kl):
            kl.remove(k1)
    print(n)
    h = h * 10
    t = t * 10 + 9
    print(h, t)

