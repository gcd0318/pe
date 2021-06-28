"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
"""

import math

def isp(s):
    return (len(s) <= 1) or ((s[0] == s[-1]) and (isp(s[1:-1])))


def pless(n):
    resl = []
    biggest = 1
    i = math.ceil(math.log(n, 2))
    for j in range(0, i - 2):
        for k in range(j + 2, i + 1):
            p = (k * (k + 1) * (2 * k + 1) - j * (j + 1) * ( 2 * j + 1)) // 6
            if (p <= n) and (isp(str(p))) and (not(p in resl)):
                resl.append(p)
    return resl

N = 10 ** 8
#N = 1000

ps = pless(N)
ps.sort()
print(ps, len(ps), sum(ps))
