"""


Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

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

sql = []
for x in range(1, 10):
    s = str(x*x)
    if(x <= 3):
        s = '0' + s
    sql.append(s)
tl = []
sqs = set(sql)

c = 0
#ls = select(6, range(10))
ls = select(6, '1234567890')
rl = []
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        ssi = ls[i]
        ssj = ls[j]
        if('6' in ssi)or('9' in ssi):
            ssi = ssi + ['6','9']
        sssi = set(ssi)
        if('6' in ssj)or('9' in ssj):
            ssj = ssj + ['6','9']
        sssj = set(ssj)
        us = []
        for xi in sssi:
            for xj in sssj:
                si = str(xi)
                sj = str(xj)
#                s = si + sj
                us.append(si + sj)
                us.append(sj + si)
#        print(set(us))
#        print(ssi, ssj, sqs.issubset(set(us)))
        sus = set(us)
        if sqs.issubset(sus):
            ssi.sort()
            ssj.sort()
            sss = [''.join(ssi) + ''.join(ssj), ''.join(ssj) + ''.join(ssi)]
            rl = rl + sss
rs = set(rl)
print(len(rs)//2)
