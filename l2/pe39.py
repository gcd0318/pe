"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
"""

def p2abc(p):
    res = []
    for a in range(1, p-2):
        for b in range(a, p-1):
            if(a**2+b**2 == (p-a-b)**2):
                res.append([a, b, p-a-b])
    return len(res)

d = {}
for i in range(1, 1000+1):
    d[p2abc(i)] = i
print(d[max(d)])
