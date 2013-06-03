"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def allInList(l, s):
    i = 0
    while((i < len(s))and(s[i] in l)):
        i = i + 1
    return(len(s) == i)

x = 1
i = 1
t = i
s = str(i)
l = list(s)
while(x < 6):
    s = str(i)
    l = list(s)
    if(allInList(l, str(t))):
        if(125874 == i):
            print(i, t)
        t = t + i
        x = x + 1
    else:
        i = i + 1
        if((1 < int(s[0]))):
            i = 10**len(s)
        t = i
        x = 1
print(i)
