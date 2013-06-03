"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def sumOfR(x, n):
    l = []
    for c in str(x):
        l.append(int(c))
    res = 0
    for i in l:
        res = res + i**n
    return res

def isSumOfR(x, n):
    return (x==sumOfR(x, n))

def nOfD(t):
    x = 0
    tmp = 1
    while(tmp <= t):
        tmp = tmp * 10
        x = x + 1
    if(0 == x):
        x = 1
    return x

def upperBoundOfR(n):
    t = 0
    k = 1
    while(t < k):
        t = t*10+9
        x = nOfD(t)
        k = (9**n)*x
    return (10**x)

print(upperBoundOfR(5))

res = 0
for i in range(2, upperBoundOfR(5)):
    if(isSumOfR(i, 5)):
        res = res + i
        print(i)
print(res)
