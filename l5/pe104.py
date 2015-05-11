"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""

def fib(n):
    res = 1
    if(n > 2):
        res = fib(n-1) + fib(n-2)
    return res

def is_pd(x):
    return set(x)==set('123456789')

prev = 1
pprev = 0
fi = 1

n = 1
i = 1
while(not(is_pd(str(fi)[:9])))or(not(is_pd(str(fi)[-9:]))):
    while(i < n):
        i = i + 1
        fi = prev + pprev
        pprev = prev
        prev = fi
    n = n + 1
print(i)
