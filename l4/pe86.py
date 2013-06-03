"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds one million.
"""
import math

def shortest2(a, b, c):
    l = [a, b, c]
    l.sort()
    return (l[0]+l[1])**2 + l[2]**2

def rootIsInt(x):
    return (math.ceil(math.sqrt(x)))**2 == x

def routes(s, e):
    res = 0
    for a in range(1, e+1):
        for b in range(a, e+1):
            for c in range(max(s+1, b), e+1):
                if rootIsInt(shortest2(a, b, c)):
                    res = res + 1
    return res

M = 1000000
n = 100
rn = 2060
while(rn <= M):
    n = n + 1
    rn = rn + routes(n-1, n)
print(n)
