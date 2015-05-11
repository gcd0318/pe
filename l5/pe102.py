"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""

def oriIsSameSide(x1, y1, x2, y2, x3, y3):
    return (y1*(x2-x1)-x1*(y2-y1))*((x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)) > 0

def oriIsIn(x1, y1, x2, y2, x3, y3):
    res = True
    i = 0
    while(res and(i < 3)):
        res = res and oriIsSameSide(x1, y1, x2, y2, x3, y3)
        tx = x1
        ty = y1
        x1 = x2
        y1 = y2
        x2 = x3
        y2 = y3
        x3 = tx
        y3 = ty
        i = i + 1
    return res

f = open('triangles.txt', 'r')
ls = f.readlines()
f.close()

i = 0
for l in ls:
    sx1, sy1, sx2, sy2, sx3, sy3 = l.strip().split(',')
    x1 = int(sx1)
    y1 = int(sy1)
    x2 = int(sx2)
    y2 = int(sy2)
    x3 = int(sx3)
    y3 = int(sy3)

    if oriIsIn(x1, y1, x2, y2, x3, y3):
        i = i + 1
print(i)
