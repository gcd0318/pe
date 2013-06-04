"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

	
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

def cost(x, y, d, rd):
    i = 100*x+y
    if(i in rd):
        return rd[i]
    elif(0 == x):
        if(0 == y):
            res = d[x][y]
        else:
            res = cost(x, y-1, d, rd) + d[x][y]
    else:
        if(0 == y):
            res = cost(x-1, y, d, rd) + d[x][y]
        else:
            res = min(cost(x-1, y, d, rd), cost(x, y-1, d, rd)) + d[x][y]
    rd[i] = res 
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

print(cost(79, 79, square, {}))
