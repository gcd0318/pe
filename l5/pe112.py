"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
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

def part(p):
    r = 0
    i = 0
    b = 0
    while r < p:
        i = i + 1
        if bou(i):
            b = b + 1
            r = b / i
    return i

print(part(0.99))