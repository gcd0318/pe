"""
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ways of doing this.

p114.png
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).
"""

d = {}

def g(n):
    res = 1
    if n in d:
        res = d[n]
    elif (2 < n):
        if (3 == n):
            res = 2
        else:
            res = g(n-1) + n - 2
        for i in range(4, n-2):
            res = res + g(n-i) - 1
 #   print(n, res)
    d[n] = res
    return res

n = 50
print(g(n))
