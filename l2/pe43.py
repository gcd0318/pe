"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2 
d3d4d5=063 is divisible by 3 
d4d5d6=635 is divisible by 5 
d5d6d7=357 is divisible by 7 
d6d7d8=572 is divisible by 11 
d7d8d9=728 is divisible by 13 
d8d9d10=289 is divisible by 17 
Find the sum of all 0 to 9 pandigital numbers with this property.
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

tl = permute(list('0123456789'))

l = []
for i in tl:
    if((0 == int(i[3])%2)and(0 == int(i[5])%5)and(0 ==(int(i[2])+int(i[3])+int(i[4]))%3)and(not(i.startswith('0')))):
        l.append(i)

pl = lessPrime(17+1)

tot = 0
for i in l:
    res = True
    j = 4
    while(res and (j < 8)):
        d = int(i[j: j + 3])
        res = res and(0 == d%(pl[j-1]))
        j = j + 1
    if(res):
        tot = tot + int(i)

print(tot)
