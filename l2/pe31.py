"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
"""
import math

def lower(n, l):
    i = 0
    if(1 >= n):
        return 0
    else:
        while((l[i] < n)and(i < len(l))):
            i = i + 1
        return(l[i-1])

def sep(n, ub, cl):
    res = 0
    while(ub > n):
        ub = lower(ub, cl)
    if(1 >= n):
        return 1
    elif(1 == ub):
        res = res + 1
    elif(2 == ub):
        res = res + math.floor(n/2)+1
    else:
        low = lower(n, cl)
        while(low > ub):
            low = lower(low, cl)
        t = math.floor(n/low)
        for i in range(0, t+1):
            llow = lower(low, cl)
#            print(i, n-i*low, llow, sep(n-i*low, llow, cl))
            res = res + sep(n-i*low, llow, cl)
        if(ub >= n):
            res = res + int(n in cl)
    return res

cl = [1,2,5,10,20,50,100,200]
d = {}
cl.sort()

print(sep(200, 200, cl))
