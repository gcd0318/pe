"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math

def sumOfDiv(n):
    res = set([])
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if((0 == n % i)and(i != n)):
            res.add(i)
            if(1 != i):
                res.add(int(n/i))
    return sum(res)

def isPerf(n):
    return (sumOfDiv(n) == n)

def isDeficient(n):
    return(sumOfDiv(n) < n)

def isAbundant(n):
    return(sumOfDiv(n) > n)

def lessAbundant(n):
    res = []
    for i in range(1, n):
        if(isAbundant(i)):
            res.append(i)
    res.sort()
    return res

l = lessAbundant(28123+1)
al = set([])

for i in range(0, len(l)):
    for j in range(i, len(l)):
        x = l[i]+l[j]
        if(28123 >= x):
            al.add(x)

tot = 0
for i in range(1, 28123+1):
    if(not(i in al)):
        tot = tot + i

print (tot)
