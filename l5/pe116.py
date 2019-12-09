"""
A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

png116_1.png
If green tiles are chosen there are three ways.

png116_2.png
And if blue tiles are chosen there are two ways.

png116_3.png
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
"""

import math

R = 2
G = 3
B = 4

def order(a, b):
    return math.factorial(a+b) // (math.factorial(a ) * math.factorial(b))

def cover(n, m):
    res = 0
    i = 1
    while m*i <= n:
        res = res + order(n - m*i, i)
        i = i + 1
    return res

N = 50

ttl = 0
for c in (R, G, B):
    r = cover(N, c)
    print(c, r)
    ttl = ttl + r

print(ttl)