"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

def voc(c):
    return (ord(c)-ord('A')+1)

def vow(word):
    res = 0
    for c in word:
        res = res + voc(c)
    return res

f = open("pe42_words.txt", "r")
l = f.readlines()
f.close()
s = l.pop()
s = s.replace('"', '')
wl = s.split(",")

i = 0
j = 0
tn = []
tot = 0
for w in wl:
    v = vow(w)
    while(j < v):
        i = i + 1
        j = j + i
        tn.append(j)
    if(v in tn):
        tot = tot + 1
print(tot)
