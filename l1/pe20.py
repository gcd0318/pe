"""
n! means n  (n  1)  ...  3  2  1

Find the sum of the digits in the number 100!
"""
import math

def intoPrime(n):
    half = math.floor(math.sqrt(n))
    l = [0, 0]
    for i in range(2, half+1):
        l.append(i)
    i = 0
    while (i < len(l)):
        t = i
        if (0 != l[i]):
            while(t + i < len(l)):
                t = t + i
                l[t] = 0
        i = i + 1
    i = 0
    while((0 < len(l))and((0 == i)or(0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(int(n/i))
    return [n]

def prime_rate(x):
    l = intoPrime(x)
    d = {}
    for i in l:
        d[i] = 0
    for i in l:
        r = 0
        t = x
        while(0 == t % i):
            r = r + 1
            t = int(t/i)
        d[i] = r
    return d

s = str(int(math.factorial(100)))
tot = 0
for i in s:
    tot = tot + int(i)

print (tot)

d = {}

for i in range(2, 100+1):
    di = prime_rate(i)
#    print (i, di)
    for x in di:
        if x in d:
            d[x] = d[x] + di[x]
        else:
            d[x] = di[x]
while(0 != d[2]*d[5]):
    d[2] = d[2] - 1
    d[5] = d[5] - 1

prod = 1
for i in d:
    prod = prod * (i**d[i])

l = str(int(prod)).replace('0', '')
s = 0

for i in l:
    s = s + int(i)
print (s)
