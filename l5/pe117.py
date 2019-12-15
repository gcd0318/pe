"""
Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
"""

import math

D = 1
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

d = {1:1, 2:2, 3:4, 4:8, 5:15}

def tile(n):
    res = 0
    if n in d:
        res = d[n]
    else:
        for c in (D, R, G, B):
            res = res + tile(n - c)
        d[n] = res
    return res


N = 50

print(tile(N))
