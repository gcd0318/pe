"""
Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
"""

import math

R = 2
G = 3
B = 4

def order(a, b):
    return math.factorial(a+b) // (math.factorial(a ) * math.factorial(b))

def tile(n):
    if n in d:
        res = d[n]
    else:
        res = 1
        for c in (R, G, B):
            if (c <= n):
                for 

        d[n] = res

    return res



N = 50

ttl = 0
for c in (R, G, B):
    r = cover(N, c)
    print(c, r)
    ttl = ttl + r

print(ttl)
