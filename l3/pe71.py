"""
Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""

def less(a, b):
    return a[0]*b[1] < a[1]*b[0]
def larger(a, b):
    return less(b, a)
def equal(a, b):
    return a[0]*b[1] == a[1]*b[0]
def gcd(m, n):
    if(m > n):
        return gcd(n, m)
    if(0 == m):
        return n
    return gcd(n % m, m)
def rpfize(f):
    hcf = gcd(f[0],f[1])
    return [f[0]//hcf, f[1]//hcf]

def order(fl, h, t):
    pass

N = 1000000
#N = 200
#lp = lessPrime(7*N)

for i in range(3*N-7, 3*N):
    if i%7==0:
        tup = i//7

f = rpfize([tup, N])
for i in range(2, N+1):
    down = N - i + 2
    for up in range(1+tup*down//(7*N), 1+down//2):
        if (less([tup, N], [up, down])and(less([up, down], [3*N, 7*N]))):
            tf = rpfize([up, down])
            if less(f, tf):
                f = tf + []
print(f)
