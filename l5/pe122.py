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
    while((0 < len(l))and((0 == i)or(0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(int(n/i))
    return [n]

def primeRate(nlp, n):
    d = {}
    for i in nlp:
        d[i] = 0
    for np in nlp:
        r = 0
        t = n
        while(0 == t % np):
            r = r + 1
            t = int(t/np)
        d[np] = r
    return d

def prime_rate(n):
    return primeRate(intoPrime(n), n)


def sum_m(x):
    d = {1: [1]}
    for i in range(2, x + 1):
        d[i] = d[i - 1] + [i]
        if (0 == i % 2):
            if len(d[i // 2]) < len(d[i - 1]):
                d[i] = d[i // 2] + [i]
        else:
            for j in range(1, i // 2 + 1):
                cand = list(set(d[j] + d[i - j]))
                if len(d[i - 1]) < len(cand):
                    d[i] = cand + [i]
    return d




T = 200

l = []
for i in range(T + 1):
    l.append(list(range(1, i + 1)))

for i in range(T + 1):
    for j in l[i]:
        if (i + j <= T) and (len(l[i]) + 1 < len(l[i + j])):
            l[i + j] = l[i] + [i + j]




"""
for i in range(2, T):
    cand = l[i] + [i + 1]
    if len(l[i + 1]) >= len(cand):
        l[i + 1] = cand
    t = 2
    j = i * t
    cand = l[i] + [j]
    while(j <= T):
        if len(cand) <= len(l[j]):
            l[j] = cand + []
        t = t + 1
        j = i * t
        cand.append(j)

for i in range(2, T):
    tl = l[i]
    for j in range(1, len(tl)):
        for k in range(len(tl)):
            l[tl[j]] + l[tl[j]]



        




um = sum_m(T)
for i in range(1, T + 1):
    print(i, len(sm[i]) - 1, sm[i])
"""

for i in range(len(l)):
    print(i, len(l[i]) - 1, l[i])


s = 0
for tl in l:
    if (0 < len(tl)):
        s = s + len(tl) - 1
print(s)
