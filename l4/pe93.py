"""


By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""

import math

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

def calc4(s):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    l = [a, b, c, d]
    l.reverse()
    res = l.pop()
    for c in s[4:]:
        if(c == '+'):
            res = res + l.pop()
        elif(c == '-'):
            res = res - l.pop()
        elif(c == '*'):
            res = res * l.pop()
        elif(c == '/'):
            res = res / l.pop()
    return res

def allRs(l):
#    print(l)
    resl = []
    for i in permute(list(l)):
        tl = []
        for t in select(3, list('+-*/'*3)):
            tl.append(''.join(t))
        for j in set(tl):
            res = calc4(i+''.join(j))
            r = math.ceil(res)
            if(r == math.floor(res)):
                if(r > 0):
                    resl.append(r)
                else:
                    resl.append(-1*r)
    resl = list(set(resl))
    resl.sort
    return resl

def longOrder(l):
    if(len(l) <= 1):
        res = len(l)
    else:
        l1 = l[0]
        l2 = l[1]
        i = 2
        while((l2-l1 == 1)and(i < len(l))):
            l1 = l2
            l2 = l[i]
            i = i + 1
        res = i - 1
    return res

ml = 0
for l in select(4, list('123456789')):
    rl = allRs(l)
    length = longOrder(rl)
    if(ml < length):
        ml = length
        l.sort()
        res = ''.join(l)
print(res)
