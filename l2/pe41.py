"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

def isPan(n):
    s = str(n)
    i = 1
    while(i < len(s)):
        if(str(i) in s):
            i = i + 1
        else:
            return False
    return True

pl = lessPrime(7654321+1)

i = len(pl) - 1
while(not(isPan(pl[i]))):
    i = i - 1
print(pl[i])
