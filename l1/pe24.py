"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math

def p(m, n):
    return int((math.factorial(n))/(math.factorial(n - m)))

def sigmaP(n):
    tot = 0
    for i in range(1, n+1):
        tot = tot + p(i, i)
    return tot

def nop(l, k):
    tl = l
    nov = len(l)
    tl.sort()
    d={}
    for i in range(0, len(l)):
        d[i] = l[i]
    if(p(nov, nov) < k):
        return None
    elif(p(nov, nov) == k):
        res = ''
        while(0 < len(tl)):
            res = res + str(tl.pop())
        return res
    else:
        less = p(nov-1, nov-1)
        c = 0
        t = k
        while(less < t):
            t = t - less
            c = c + 1
        tl.remove(d[c])
        return (str(d[c])+nop(tl, t))



l = [0,1,2,3,4,5,6,7,8,9]
e = 1000000
print(nop(l, e))
