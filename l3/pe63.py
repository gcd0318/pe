"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

c = 0
t = 1
i = 1
p = i**t
while(len(str(p)) <= t):
    if(len(str(p)) == t):
        c = c + 1
        t = t + 1
    else:
        i = i + 1
        t = 1
    p = i**t
print(c)
