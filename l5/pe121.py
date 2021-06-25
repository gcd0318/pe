"""
A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
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
    while((0 < len(l))and((0 == i)or(0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(int(n/i))
    return [n]

def prime_rate(x):
    l = intoPrime(x)
    d = {}
    for i in l:
        d[i] = 0
    for i in l:
        r = 0
        t = x
        while(0 == t % i):
            r = r + 1
            t = int(t/i)
        d[i] = r
    return d

def rate_add(r1, r2):
    return [r1[0] * r2[1] + r1[1] * r2[0], r1[1] * r2[1]]
#    return reduct([r1[0] * r2[1] + r1[1] * r2[0], r1[1] * r2[1]])

def rate_mul(r1, r2):
    return r1[0] * r2[0], r1[1] * r2[1]]
#    return reduct([r1[0] * r2[0], r1[1] * r2[1]])

def i2bs(i, length):
    s = str(bin(i))[2:]
    return '0' * (length - len(s)) + s

def ones(s):
    res = 0
    for c in s:
        if ('1' == c):
            res = res + 1
    return res

def reduct(r):
    res = [r[0], r[1]]
    if(1 < res[0]):
        for p in intoPrime(res[0]):
            while (0 == res[1] % p) and (0 == res[0] % p):
                res = [res[0] // p, res[1] // p]
    return res



def win_pick(rounds):
    wins = rounds // 2 + 1
    rates = [0, 1]
    for i in range(2 ** rounds):
        rate = [1, 1]
        bs = i2bs(i, rounds)
        if ones(bs) >= wins:
            for c in range(len(bs)):
                if ('1' == bs[c]):
                    rate = rate_mul(rate, (1, c + 2))
                else:
                    rate = rate_mul(rate, (c + 1, c + 2))
                c = c + 1
            rates = rate_add(rates, rate)
    return rates


def rate(rounds):
    wins = rounds // 2 + 1
    for r in range(1, rounds + 1):
        win_rate = (1, r + 1)



def win_pick_f(rounds):
    wins = rounds // 2 + 1
    rates = 0
    for i in range(2 ** rounds):
        rate = 1
        bs = i2bs(i, rounds)
        if ones(bs) >= wins:
            for c in range(len(bs)):
                if ('1' == bs[c]):
                    rate = rate * Fraction(1, c + 2)
                else:
                    rate = rate * Fraction(c + 1, c + 2)
                c = c + 1
            rates = rates + rate
    return rates



wp  = win_pick(15)
print(wp)
print(wp[1] // wp[0])
