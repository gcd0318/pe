"""
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.
"""

d = {}

def g(m, n):
    res = 1
    if (m in d) and (n in d[m]):
        res = d[m][n]
    else:
        if not(m in d):
            d[m] = {}
        if (m <= n):
            if (m == n):
                res = 2
            else:
                res = g(m, n-1) + n - m + 1
            for i in range(m+1, n-m+1):
                res = res + g(m, n-i) - 1
 #   print(n, res)
    d[m][n] = res
    return res

N = 1000000
m = 50
n = m
while (g(m, n) < N):
    n = n + 1
print(n)