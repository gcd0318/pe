"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

def catl(l1, l2):
    res = l1 + l2
    return list(set(res))

def isBelow(x, y, d):
    if not(y in d[x]):
        i = 0
        while(i < len(d[x])):
            return isBelow(d[x][i], y, d)
        return False
    return True
        
f = open('keylog.txt', 'r')
ls = f.readlines()
f.close()

d = {}
for i in range(10):
    d[i] = []
for s in ls:
    l = []
    for c in s.strip():
        l.append(int(c))
    d[l[0]] = catl(d[l[0]], [l[1], l[2]])
    d[l[1]] = catl(d[l[1]], [l[2]])

for k in d:
    i = 0
    while(i < len(d[k])-1):
        j = i + 1
        while(j < len(d[k])):
            if isBelow(d[k][i], d[k][j], d):
                d[k].remove(d[k][j])
            elif isBelow(d[k][j], d[k][i], d):
                d[k].remove(d[k][i])
            else:
                j = j + 1
        i = i + 1

td = {}
for i in d:
    if(0 < len(d[i])):
        td[i] = d[i][0]
for i in list(d.keys()):
    if((not(i in list(td.values())))and(0 == len(d[i]))):
        d.pop(i)
l = []
for i in range(10):
    if (i in d):
        l.append(i)

i = 0
while(i < len(l)-1):
    j = i + 1
    while(j < len(l)):
        if isBelow(l[j], l[i], d):
            t = l[i]
            l[i] = l[j]
            l[j] = t
        j = j + 1
    i = i + 1

res = 0
for i in l:
    res = res*10 + i
print(res)
