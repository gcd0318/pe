"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

N = 1000000
lp = lessPrime(N)

maxl = 0
tot = 0
while(tot < lp[-1]):
    maxl = maxl + 1
    tot = tot + lp[maxl]

i = 0
tot = 0
while((not(tot in lp))and(i < maxl)):
    length = maxl - i
    j = 0
    tot = 0
    while((not(tot in lp))and(length+j < len(lp))and(tot < lp[-1])):
        tot = sum(lp[j:length+j])
        if(not(tot in lp)):
            j = j + 1
                
    i = i + 1
print(length, tot)
