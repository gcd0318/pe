"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

import math

def lessPrime(n):
    res = []
    l = [0,0]
    for i in range(2, n+1):
        l.append(i)
    for i in l:
        t = i
        while ((0 != l[i])and(t+i < len(l))):
            t = t + i
            l[t] = 0
    for i in l:
        if(0 != i):
            res.append(i)
    return res

lp = lessPrime(101)
def w2p(w):
    res = 1
    for c in w:
        res = res * lp[ord(c) - ord('A')]
    return res

f = open('words.txt', 'r')
ls = f.readlines()
f.close()
words = []
for l in ls:
    l = l.replace('"', '')
    words = words + l.split(',')

d = {}
for w in words:
    p = w2p(w)
    if(p in d):
        d[p].append(w)
    else:
        d[p] = [w]
ps = []
for k in d:
    if(len(d[k]) > 1):
        ps.append(d[k])
m = 0
for p in ps:
    l = len(p[0])
    for i in range(math.ceil(math.sqrt(10**(l-1))), math.ceil(math.sqrt(10**l-1))):
        s = str(i**2)
        d = {}
        j = 0
        while j in range(l):
            if(not(p[0][j] in d)):
                if(not(s[j] in d.values())):
                    d[p[0][j]] = s[j]
                else:
                    j = l
            elif(d[p[0][j]] != s[j]):
                j = l
            j = j + 1
        if(len(d) == len(set(list(p[0])))):
            ts = ''
            for c in p[1]:
                ts = ts + d[c]
            t = int(ts)
            if((ts == str(t))and(t//math.ceil(math.sqrt(t)) == math.ceil(math.sqrt(t)))):
                tm = max(int(s), t)
                if(tm > m):
                    m = tm
print(m)
