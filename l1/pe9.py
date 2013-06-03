"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def isPyth(a, b, c):
    return (a*a + b*b == c*c)

for i in range(1, 1000-3+1):
    for j in range(i, 1000-3+1+1):
            if (isPyth(i, j, 1000-i-j)):
                print (i*j*(1000-i-j))
