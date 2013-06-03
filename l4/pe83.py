"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

	
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

def mmax(ll):
    res = max(ll[0])
    for l in ll:
        m = max(l)
        if(res < m):
            res = m
    return res

def cost(x, y, d, rd, base):
    N = len(d)
    M = mmax(d)*N*N
    res = M + 1
    ps = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
    i = (10**base)*x + y
    if((0 == x)and(1 == y))or((0 == y)and(1 == x)):
        res = d[x][y] + d[0][0]
    else:
        if(i in rd):
            return rd[i]
        else:
            rd[i] = M + 1
        rs = [rd[i]]
        for [ex, ey] in ps:
            if(0 <= ex)and(0 <= ey)and(ex < N)and(ey < N):
                ei = c2p([ex, ey], base)
                rs.append(cost(ex, ey, d, rd, base))
#                print(ex, ey, 'for', x, y)
        res = min(rs) + d[x][y]
    rd[i] = res
    return res

def p2c(se, base):
    sse = str(se)
    while(len(sse) < base*2):
        sse = '0' + sse
    sx = int(sse[:base])
    sy = int(sse[-base:])
    return [sx, sy]

def c2p(pl, base):
    ex, ey = pl
    return (10**base)*ex+ey

def reset(d, rd, base):
    ng = True
    while(ng):
        ng = False
        for i in rd:
            [x, y] = p2c(i, base)
            ps = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
            for[ex, ey] in ps:
                if(0 <= ex)and(0 <= ey)and(ex < N)and(ey < N):
                    ei = c2p([ex, ey], base)
#                    print(ex, ey, ei, rd, d)
                    tv = d[x][y] + rd[ei]
                    if(tv < rd[i]):
                        rd[i] = tv
                        ng = True
    return ng

f = open('matrix.txt', 'r')
ls = f.readlines()
f.close()

square = []
for l in ls:
    tl = []
    for s in l.strip().split(','):
        tl.append(int(s))
    square.append(tl)

N = len(square)
base = len(str(N))
M = mmax(square)*N*N
rd = {0:square[0][0], 1:square[0][1]+square[0][0], 100:square[1][0]+square[0][0]}
for x in range(N):
    for y in range(N):
        i = c2p([x, y], base)
        if not(i in rd):
            rd[i] = M
#print(rd)
#print(cost(2,4, square, rd, base))
#cost(N-1, N-1, square, rd, base)
reset(square, rd, base)
i = (N-1)*(10**base) + N-1
print(i, rd[i])
