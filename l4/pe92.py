"""


A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

d = {1:1, 89:89}

def calc(n):
    s = str(n)
    res = 0
    for c in s:
        res = res + int(c)**2
    return res

def chain(n):
    rl = [1, 89]
    res = n
    resl = [n]
    while((not(res in rl))and(not(res in d))):
        resl.append(res)
        res = calc(res)
    for x in resl:
        d[x] = d[res]
    return d[res]



c = 0
N = 10000000

for i in range(1, N):
    if(chain(i) == 89):
        c = c + 1

print(c)
