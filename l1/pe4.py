"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isCycle(aStr):
    if (len(aStr) <= 1):
        return True
    else:
        return ((aStr[0] == aStr[-1])and isCycle(aStr[1:-1]))

l = []
n = 0
for i in range(100*100, 999*999):
    if (isCycle(str(i))):
        l.append(i)

res = []
while ((0 < len(l))and(0 == len(res))):
    n = l.pop()
    i = 100
    while ((i < 1000)and(0 == len(res))):
        if ((0 == n % i)and(n/i<1000)and(n/i>99)):
            res = [n, i, int(n/i)]
            print (res)
        else:
            i = i + 1
