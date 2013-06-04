"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

	
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""

def mmax(ll):
    res = max(ll[0])
    for l in ll:
        m = max(l)
        if(res < m):
            res = m
    return res

def c2p(pl):
    sx, sy, ex, ey = pl
    return 1000000*sx+10000*sy+100*ex+ey

def p2c(se, base):
    sse = str(se)
    while(len(sse) < base*4):
        sse = '0' + sse
#    print(sse)
    sx = int(sse[:base])
    sy = int(sse[base:base*2])
    ex = int(sse[base*2:base*3])
    ey = int(sse[-base:])
#    print([sx, sy, ex, ey])
    return [sx, sy, ex, ey]

def cost(pl, ds, rd, pd):
#    print('get in', pl)
    sx, sy, ex, ey = pl
    N = len(ds)
    i = c2p(pl)
    if not(i in pd):
        pd[i] = []
    N = len(ds)
    base = len(str(N))+1
    M = mmax(ds)*N*N
    res = M
    if(sx == ex)and(sy == ey):
        res = ds[sx][sy]
    elif((sx == ex)and(1 == ey - sy))or((sy == ey)and((sx - ex)in[1,-1])):
#        print('one step')
        res = ds[sx][sy] + ds[ex][ey]
    else:
        if(3 == len(pd[i])):
            print(rd)
            print(pd[ex][ey])
            return rd[i]
        else:
            if(0 <= ex)and(0 <= ey)and(sy <= ey):
                if not(i in rd):
                    rd[i] = M
                ps = []
                if(0 < ey):
                    ps.append(c2p([sx, sy, ex, ey-1]))
                t = c2p([sx, sy, ex-1, ey])
                if(0 < ex)and((not(t in rd))or((t in rd)and(rd[t] < M))):
                    ps.append(t)
                t = c2p([sx, sy, ex+1, ey])
                if(ex < N-1)and((not(t in rd))or((t in rd)and(rd[t] < M))):
                    ps.append(t)
 #               print('ps of',pl, ':',ps, rd)
                pls = [rd[i]]
                for p in ps:
                    if not(p in pd[ex][ey]):
 #                       print(sx, sy, ex, ey, ps, pd, pls)
                        pls.append(cost(p2c(p, base), ds, rd, pd) + ds[ex][ey])
                        pd[ex][ey].append(p)
 #                   print('==================in for')
                res = min(pls)
    rd[i] = res
#    print('+++++++++++++++++++', pl, res)
    return res


f = open('matrix.txt', 'r')
ls = f.readlines()
f.close()

square = []
for l in ls:
    tl = []
    for s in l.strip().split(','):
        tl.append(int(s))
    square.append(tl)

d = {}
N = len(square)
pd = {}
for i in range(N):
    for j
    pd.append(tl+[])

M = mmax(square)*N*N
mc = M
"""
print(cost([0,0,0,3],square, d, pd))
"""
for sx in range(N):
    for ex in range(sx, N):
        c = cost([sx, 0, ex, N-1], square, d, pd)
#        print('a new start', sx, ex, c)
        if(mc > c):
            mc = c
for i in d:
    print(i, d[i])
print(mc)
