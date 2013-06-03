"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def isL(n):
    if(10 > n):
        return isPrime(n)
    else:
        s = str(n)
        return(isPrime(n) and isL(int(s[1:])))
    
def isR(n):
    if(10 > n):
        return isPrime(n)
    else:
        s = str(n)
        return(isPrime(n) and isR(int(s[:-1])))

def isT(n):
    return(isL(n) and isR(n))

def primeDigitTop2(n):
    s = str(n)
    i = 1
    lh = [2,3,5,7]
    lt = [3,7]
    lm = [1,3,7,9]
    if((int(s[0])in lh)and(int(s[-1])in lt)):
        while(i < len(s)-1):
            if(int(s[i])in lm):
                i = i + 1
            else:
                return False
        return True
    else:
        return False
        
i = 0
j = 11
tot = 0
while(11 > i):
    s = str(j)
    c = 0
    if(primeDigitTop2(j)):
        if(isT(j)):
            print(j)
            tot = tot + j
            i = i + 1
    j = j + 2

print(tot)
