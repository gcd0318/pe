"""
The following undirected network consists of seven vertices and twelve edges with a total weight of 243.


The same network can be represented by the matrix below.

        A       B       C       D       E       F       G
A       -       16      12      21      -       -       -
B       16      -       -       17      20      -       -
C       12      -       -       28      -       31      -
D       21      17      28      -       18      19      23
E       -       20      -       18      -       -       11
F       -       -       31      19      -       -       27
G       -       -       -       23      11      27      -
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
"""

from copy import deepcopy

def get_map(fn):
    with open(fn, 'r') as f:
        ls = f.readlines()
    linelist = []
    for l in ls:
        l = l.strip()
        tmpl = []
        for edge in l.split(','):
            if ('-' != edge):
                tmpl.append(int(edge))
            else:
                tmpl.append(0)
        linelist.append(tmpl)
    return linelist



def map2d(linelist):
    resd = {}
    for i in range(len(linelist)):
        line = linelist[i]
        tmpd = {}
        for j in range(len(line)):
            edge = line[j]
            if (0 != edge) and ((not(j in resd)) or (not(i in resd[j]))):
                tmpd[j] = edge
#        if (0 < len(tmpd)):
#            resd[i] = tmpd
        resd[i] = tmpd
    return resd

def same_list(l1, l2):
    res = (len(l1) == len(l2))
    i = 0
    while (i < len(l1)) and res:
        res = l1[i] in l2
        i = i + 1
    return res

def all_connected(mapd):
    nodes = list(mapd.keys())
    resl = []
    tmpl = []
    if nodes:
        resl.append(nodes[0])
    while not same_list(tmpl, resl):
        i = 0
        while(i < len(resl)):
            node = resl[i]
            if(not(node in resl)) and (0 < len(mapd[node])):
                resl.append(node)
            for n in mapd[node]:
                if not(n in resl):
                    resl.append(n)
            i = i + 1
        tmpl = deepcopy(resl)
        for node in mapd:
            if not(node in resl):
                for n in mapd[node]:
                    if n in resl:
                        if not(node in resl):
                            resl.append(node)


    res = True
    all_nodes = list(mapd.keys())
    i = 0
    while res and (i < len(all_nodes)):
        res = res and (all_nodes[i] in resl)
        i = i + 1
    return res

def sumup(mapd):
    res = 0
    for node in mapd:
        res = res + sum(mapd[node].values())
    return res

def weight_dict(mapd):
    resd = {}
    for s in mapd:
        for e in mapd[s]:
            if mapd[s][e] in resd:
                resd[mapd[s][e]].append((s, e))
            else:
                resd[mapd[s][e]] = [(s, e)]
    return resd

def reduce_map(mapd):
    wd = weight_dict(mapd)
    ws = list(wd.keys())
    ws.sort(reverse=True)
    d = deepcopy(mapd)
#    print(d)
    for w in ws:
        for edge in wd[w]:
#            print(w, edge)
            tmpd = deepcopy(d)
            d[edge[0]].pop(edge[1])
#            print(tmpd)
#            print(all_connected(d))
            if all_connected(d):
                tmpd = deepcopy(d)
            else:
                d = deepcopy(tmpd)
#            print(d)
#            print(tmpd)
    return d


sample = [[0, 16, 12, 21, 0, 0, 0],
[16, 0, 0, 17, 20, 0, 0],
[12, 0, 0, 28, 0, 31, 0],
[21, 17, 28, 0, 18, 19, 23],
[0, 20, 0, 18, 0, 0, 11],
[0, 0, 31, 19, 0, 0, 27],
[0, 0, 0, 23, 11, 27, 0]]


sample_reduced = [[0,16,12,0,0,0,0],
[16,0,0,17,0,0,0],
[12,0,0,0,0,0,0,0],
[0,17,0,0,18,19,0],
[0,0,0,18,0,0,11],
[0,0,0,19,0,0,0],
[0,0,0,0,11,0,0]
]
'''
sample_reduced = [[0,16,12,0,0,0,0],
[16,0,0,17,0,0,0],
[12,0,0,0,0,0,0,0],
[0,17,0,0,18,19,0],
[0,0,0,18,0,0,0],
[0,0,0,19,0,0,0],
[0,0,0,0,0,0,0]
]
'''

maplines = get_map('pe107_network.txt')
mapd = map2d(maplines)
#mapd = map2d(sample)
mapd_reduced = reduce_map(mapd)

for node in mapd:
    print(node, mapd[node])
#print(mapd_reduced)
#print(map2d(sample_reduced))
print(all_connected(mapd))
print(all_connected(mapd_reduced))
print(sumup(mapd) - sumup(mapd_reduced))
