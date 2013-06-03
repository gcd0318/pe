"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

def voc(c):
    return (ord(c)-ord('A')+1)

def von(name):
    res = 0
    for c in name:
        res = res + voc(c)
    return res

f = open("pe22_names.txt", "r")
l = f.readlines()
f.close()

d = {}
i = 0
while(0 < len(l)):
    ln = l.pop()

    tl = ln.split(',')
    tl.sort()
    for name in tl:
        i = i + 1
        name = name.replace('"', '')
        d[i] = name

tot = 0
for j in range(1, len(d)+1):
    tot = tot + (j * von(d[j]))

print (tot)
