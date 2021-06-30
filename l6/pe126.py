"""
The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
"""

def blocks(n, a, b, c):
    face = 2 * n * (a * b + a * c + b * c)
    edge = 2 * n * (n -1) * (a + b + c)
    acme = 4 * n * (n - 1) * (n - 2) // 3
    return face + edge + acme

def cover(n, a, b, c):
    res = 0
    if 0 < n:
        res = 2 * (a * b + a * c + b * c) + 4 * (n - 1) * (a + b + c) + 4 * (n - 1) * (n - 2)
    return res

def combines(mx):
    res = []
    for i in range(1, mx + 1):
        for j in range(1, i + 1):
            res.append([mx, i, j])
    return res

def C(n):
    res = []
    mbs = n // 2 - 2
    for m in range(1, mbs):
        for a, b, c in combines(m):
            i = 1
            bs = cover(i, a, b, c)
            while bs < n:
                i = i + 1
                bs = cover(i, a, b, c)
            if bs == n:
                res.append([i, a, b, c])
#    print(n, len(res))
#    for cb in res:
#        print(cb)
#    print('=' * 10)
    return len(res)


print(C(22))
print(C(46))
print(C(78))
print(C(118))
print(C(142))
print(C(154))

N = 1000
i = 6
while C(i) != N:
    i = i + 2

print(i)
