"""

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""

N = 50

c = 0
ss = []
for x1 in range(N+1):
    for x2 in range(N+1):
        for y1 in range(N+1):
            for y2 in range(N+1):
                ss = [x1*x1+y1*y1, x2*x2+y2*y2, (x1-x2)**2+(y1-y2)**2]
                ss.sort()
                if(ss[0]>0)and(ss[2] == ss[0]+ss[1]):
                    c = c + 1
print(c//2)
