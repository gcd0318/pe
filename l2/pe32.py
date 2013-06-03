"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def isPan(n):
    s = str(n)
    res = True
    for i in range(1, len(s)+1):
        res = res and(str(i) in s)
    return res

def prodUnusual(m, n):
    return isPan(str(m)+str(n)+str(m*n))

us = set([])
for i in range(0, 10000):
    for j in range(0, 10**(5-len(str(i)))):
        k = i * j
        if((isPan(str(i)+str(j)+str(k)))and(9 == len(str(i)+str(j)+str(k)))):
            print(i, '*', j, '=', i*j)
            us.add(i*j)

print(sum(us))
