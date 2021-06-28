"""
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
Unsorted

Sorted

n


rad(n)



n


rad(n)


k
1

1

1

1

1
2

2

2

2

2
3

3

4

2

3
4

2

8

2

4
5

5

3

3

5
6

6

9

3

6
7

7

5

5

7
8

2

6

6

8
9

3

7

7

9
10

10

10

10

10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""


import math

def intoPrime(n):
    half = math.floor(math.sqrt(n))
    l = [0, 0]
    for i in range(2, half+1):
        l.append(i)
    i = 0
    while (i < len(l)):
        t = i
        if (0 != l[i]):
            while(t + i < len(l)):
                t = t + i
                l[t] = 0
        i = i + 1
    i = 0
    while((0 < len(l)) and ((0 == i) or (0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(n//i)
    return [n]

def prime_rate(x):
    d = {}
    if(1 < x):
        l = intoPrime(x)
        for i in l:
            d[i] = 0
        for i in l:
            r = 0
            t = x
            while(0 == t % i):
                r = r + 1
                t = t // i
            d[i] = r
    return d

def rad(n):
    res = 1
    if 2 <= n:
        for p in set(intoPrime(n)):
            res = res * p
    return res


def sorting(n, m=None):
    if m is None:
        m = n
    resl = []
    for i in range(1, n + 1):
        r = rad(i)
        pos = 0
        while (pos < len(resl)) and resl[pos][1] <= r:
            pos = pos + 1
        if pos == len(resl):
            resl.append((i, r))
        else:
            resl.append((0, 0))
            for mov in range(len(resl) - 2, pos - 1, -1):
                resl[mov + 1] = resl[mov]
            resl[pos] = (i, r)
        if len(resl) >= m:
            resl = resl[:m]
    return resl

A = 100000
P = 10000

print(sorting(10))
print(sorting(A, P)[-1])


