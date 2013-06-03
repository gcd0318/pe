"""
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000


where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

def isPrime1(n):
    l = [0, 0]
    if (n<2):
        return None
    
    for i in range(2, n+1):
        l.append(i)
    i = 1
    while (i < len(l)-1)and (not(0 == l[-1])):
        i = i + 1
        t = i
        if 0 != l[i]:
            while (i*t < len(l)):
                if 0 != l[i*t]:
                    l[i*t] = 0
                t = t + 1

    return (0 != l[-1])

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

def e(n, a, b):
    return((n+a)*n+b)

def nocp(a, b):
    n = 0
    while(isPrime(e(n, a, b))):
        n = n + 1
    return n

m = 0
p = 1
for a in range(-1000, 1000+1):
    for b in range(0, 1000+1):
        if(isPrime(b)):
            x = nocp(a, b)
            if(x > m):
                m = x
                p = a * b
print(p)
