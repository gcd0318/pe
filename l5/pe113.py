"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?
"""



def not_b(n):
    res = 0
    if (n <= 1):
        res = 10 **n -1
    elif (1 < n):
        l = [1] * 10
        sigmal = l + []
        for i in range(1, n):
            bakl = sigmal + []
            sigmal = []
            for j in range(len(l)):
                sigmal.append(sum(l[:j+1]))
            l = sigmal + []
        res = 2 * sum(sigmal[:-1]) -10 + sum(bakl)
    return res


def all_nb(n):
    r = 0
    for x in range(n+1):
        nb = not_b(x)
        r = r + nb
    return r

print(all_nb(100))