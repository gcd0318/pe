"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def chainLen(n):
    if(1 == n):
        return 1
    elif (0 == n%2):
        return 1 + chainLen(int(n/2))
    else:
        return 1 + chainLen(3*n+1)

def lenOfChain(n):
    l = 0
    while (1 != n):
        l = l + 1
        if (0 == n%2):
            n = int(n/2)
        else:
            n = 3*n+1
    l = l + 1
    return l

print (chainLen(13))
print (lenOfChain(13))

ceil = 1000000
ml = 0
for i in range(1, ceil):
    if lenOfChain(i) > ml:
        print (i)
    ml = max(ml, lenOfChain(i))
