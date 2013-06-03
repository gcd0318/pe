"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?
"""

def sod(x):
    s = str(x)
    tot = 0
    for c in s:
        tot = tot + int(c)
    return tot

def sod1(x):
    i = x
    tot = 0
    while(0 < i):
        tot = tot + i%10
        i = int(i/10)
    return tot

res = 0
for a in range(1, 100):
    for b in range(1, 100):
        s = sod(a**b)
        if(s > res):
            res = s
print(res)
