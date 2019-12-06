"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?
"""

def inc(n):
    res = True
    s = str(n)
    i = 0
    while res and (i < len(s)-1):
        res = s[i] <= s[i + 1]
        i = i + 1
    return res

def dec(n):
    res = True
    s = str(n)
    i = 0
    while res and (i < len(s)-1):
        res = s[i+1] <= s[i]
        i = i + 1
    return res

def bou(n):
    return not(inc(n) or dec(n))

def bou1(n):
    res = (100 >= n)
    if (100 < n):
        if inc(n % 100):
            pass



def bou2(n):
    res = n - 100
    s = str(n)
    i, j, k = 0, 1, 2
    while (0 < res) and (i < len(s)-2):
        res = res * (int(s[i]) - int(s[j])) * (int(s[j]) - int(s[k]))
        i = i + 1
        j = j + 1
        k = j + 1
    return res > 0

N = 10**10

c = 0
for i in range(1, N):
    if inc(i) or dec(i):
        c = c + 1
    if (i % 1000000 == 0):
        print(i, c)
print(c)