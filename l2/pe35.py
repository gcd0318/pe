"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

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
    l = [0,0]
    if(2 > n):
        return []
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
    res = []
    for i in l:
        if(0 != i):
            res.append(i)
    return res

def cirStr(string):
    s = string
    l = [s]
    i = 1
    while(i < len(s)):
        c = s[0]
        s = s.replace(c, '', 1)
        s = s + c
        l.append(s)
        i = i + 1
    return l

def isCirPrime(n):
    i = 0
    l = cirStr(str(n))
    while(i < len(l)):
        if(isPrime(int(l[i]))):
            i = i + 1
        else:
            return False
    return True

fl = []
pl = lessPrime(1000000)
for i in pl:
    cs = cirStr(str(i))
    j = 0
    while((j < len(cs))and(int(cs[j]) in pl)):
        j = j + 1
    if(j == len(cs)):
        fl.append(i)
print(len(fl))
