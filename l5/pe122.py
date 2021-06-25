"""
The most naive way of computing n15 requires fourteen multiplications:

n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n2
n2 × n2 = n4
n4 × n4 = n8
n8 × n4 = n12
n12 × n2 = n14
n14 × n = n15

However it is yet possible to compute it in only five multiplications:

n × n = n2
n2 × n = n3
n3 × n3 = n6
n6 × n6 = n12
n12 × n3 = n15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
"""

def short(l):
    resl = []
    for tl in l:
        if ([] == resl) or (len(resl) > len(tl)):
            resl = tl
    return resl

def refresh(al, tl):
    l = al + []
    if ([] == l) or ((len(short(l)) == len(tl)) and (not(tl in al))):
        l.append(tl)
    elif len(short(l)) >= len(tl):
        l = [tl]
    return l

T = 200

"""
l = []
for i in range(T + 1):
    l.append(list(range(1, i + 1)))

for i in range(T + 1):
    for j in l[i]:
        if (i + j <= T) and (len(l[i]) + 1 < len(l[i + j])):
            l[i + j] = l[i] + [i + j]
"""


l = []
for i in range(T + 1):
#    l.append(list(range(i)))
    l.append([])

for i in range(T + 1):
    if (0 == i):
        l[i] = [[]]
    else:
        for tl in l[i - 1]:
            ntl = tl + [i]
            if not(ntl in l[i]):
                l[i] = refresh(l[i], ntl)
#                l[i].append(ntl)
        for tl in l[i]:
            if(i + 1 <= T):
                ntl = tl + [i + 1]
                if not(ntl in l[i + 1]):
                    l[i + 1] = refresh(l[i + 1], ntl)
#                    l[i + 1].append(ntl)
            if(i * 2 <= T):
                ntl = tl + [i * 2]
                if not(ntl in l[i * 2]):
                    l[i * 2] = refresh(l[i * 2], ntl)
#                    l[i * 2].append(ntl)
            for j in tl:
                if (i + j <= T):
                    ntl = tl + [i + j]
                    if not (ntl in l[i + j]):
                        l[i + j] = refresh(l[i + j], ntl)
#                        l[i + j].append(ntl)


for i in range(len(l)):
    print(i, len(short(l[i])) - 1)#, l[i])


s = 0
for tl in l:
    stl = short(tl)
    if (0 < len(stl)):
        s = s + len(stl) - 1
print(s)


