"""
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

def allInds(s, c, h = 0):
    if(not(c in s)):
        return([])
    else:
        return([s.find(c)+h]+allInds(s[s.find(c)+1:], c, h+s.find(c)+1))

def isPrime1(n):
    l = [0, 0]
    if (n<2):
        return None
    
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

def betweenPrime(m, n):
    if(m == n):
        return []
    elif(m < n):
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
            if((0 != i)and(i > m)):
                res.append(i)
        return res
    else:
        return(betweenPrime(n, m))
    
def repInStr(s, sub):
    ls = len(s)
    lsub = len(sub)
    res = []
    if(0 == lsub):
        res.append(s)
    elif(ls == lsub):
        res.append(sub)
    elif(1 == lsub):
        for i in range(0, len(s)):
            res.append(s[:i]+sub+s[i+1:])
    elif(ls > lsub):
        res1 = repInStr(s[1:], sub)
        res2 = repInStr(s[1:], sub[1:])
        for i in res1:
            res.append(s[0]+i)
        for i in res2:
            res.append(sub[0]+i)
    return res

def replaceInStr(s):
    res = []
    r = ''
    rl = []
    for i in range(0, int(len(s)/3)):
        r = r + 'xxx'
        rl.append(r)
    for r in rl:
        for i in repInStr(s, r):
            ns = []
            for j in range(0, 9+1):
                if((not(i.endswith('x')))and(0 != int(i.replace('x', ''))%3)):
                    ns.append(i.replace('x', str(j)))
            if(0 < len(ns)):
                res.append(ns)
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
        s = l.pop()
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

def collect(l, m):
    res = []
    if((0 < m)and(m <= len(l))):
        if(1 == m):
            for i in l:
                res.append(i)
        else:
            res1 = collect(l[1:], m-1)
            res2 = collect(l[1:], m)
            for r in res1:
                res.append(l[0]+r)
            for r in res2:
                res.append(r)
    return res

def nopif(s):
    res = 0
    for i in range(0, 9+1):
        p = int(s.replace('x', str(i)))
        if(isPrime(p)):
            res = res + 1
    return res

t = 0
i = 0
start = 10000
end = 99999
N = 8
anl = []
t2 = 0

while(t < N):
    t = 0
    t2 = 0
    lp = betweenPrime(start, end)
    length = len(str(start))
    rep = ''
    repl = []
    for i in range(0, int((length-1)/3)):
        rep = rep + 'xxx'
        repl.append(rep)
    irepl = 0
    while((t < N)and(t2 <= 10-N)and(irepl < len(repl))):
        anl = []
        rep = repl[irepl]
        hl = list('0123456789')
        while(length - len(rep) > len(hl[0])):
            tl = []
            while(0 < len(hl)):
                h = hl.pop()
                for j in range(0, 9+1):
                    tl.append(h+str(j))
            hl = hl + tl
        for h in hl:
            if(0 != int(h)%3):
                anl = anl + permute(list(rep+h))
        anl = list(set(anl))
        ianl = 0
        while((t < N)and(t2 <= 10-N)and(ianl < len(anl))):
            ns = anl[ianl]
            if((not(ns.endswith('x')))and(0 != int(ns[-1])%2)and(0 !=int(ns[-1])%5)):
                k = 0
                t = 0
                t2 = 0
                while((t < N)and(t2 <= 10-N)and(10 > k)):
                    n = int(ns.replace('x', str(k)))
                    if n in lp:
                        t = t + 1
                    else:
                        t2 = t2 + 1
                    k = k + 1
                if(N > t):
                    t = 0
                    t2 = 0
            ianl = ianl + 1
        irepl = irepl + 1
    start = start * 10
    end = end * 10 + 9

for i in range(0, 9+1):
    k = int(ns.replace('x', str(i)))
    print(k, (k in lp))
