"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

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

def insertC2S(s, c, i):
    if(0 == i):
        return(c + s)
    elif(len(s) <= i):
        return(s + c)
    else:
        return(s[:i]+c+s[i:])

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

def isPrime1(n):
    l = [0, 0]
    if(n<2):
        return None
    if(0 == n % 2):
        return False
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

def isPrime(n):
    l = [0,0]
    if(2 > n):
        return None
    elif((2 < n)and(0 == n % 2)):
        return False
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

lp1 = lessPrime(1000)
lp2 = lessPrime(10000)
lp = []
for i in lp2:
    if(not(i in lp1)):
        lp.append(i)

while(0 < len(lp)):
    i = lp.pop()
    s = set([])
    sl = []
    tl = permute(list(str(i)))
    for x in tl:
        j = int(x)
        if((i == j)or(j in lp)):
            s.add(j)
            if(i != j):
                lp.remove(j)
    sl = list(s)
    if(3 <= len(sl)):
        for i in range(0, len(sl)-1):
            for j in range(i+1, len(sl)):
                if(int((sl[i]+sl[j])/2) in sl):
                    print(int((str(sl[i])+str(int(((sl[i]+sl[j])/2)))+str(sl[j]))))
