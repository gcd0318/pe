"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

def d2b1(n):
    if(0 == n):
        return('0')
    else:
        x = n
        res = ''
        while(0 < x):
            r = x % 2
            x = int(x/2)
            res = str(r)+res
        return res

def d2b(n):
    res = bin(n)[2:]
    while(8 > len(res)):
        res = '0' + res
    return res
    
def xor(a, b):
    if(a > b):
        return xor(b, a)
    else:
        res = ''
        xa = d2b(a)
        xb = d2b(b)
        d = len(xb) - len(xa)
        res = xb[:d]
        xb = xb[d:]
        i = 0
        while(i < len(xa)):
            if(xa[i] != xb[i]):
                res = res + '1'
            else:
                res = res + '0'
            i = i + 1
        return res

def b2d(x):
    res = 0
    b = 1
    i = len(x) - 1
    while(0 <= i):
        res = res + int(x[i]) * b
        i = i - 1
        b = b * 2
    return res

def b2d1(x):
    res = ''
    xx = x
    while(0 < len(xx)):
        while(8 > len(xx)):
            xx = '0' + xx
        res = str(int(xx[-8:], 2)) + res
        xx = xx[:-8]
    return res

def allInList(s, l):
    res = True
    i = 0
    while((i < len(s))and(res)):
        res = res and(s[i] in l)
        i = i + 1
    return res


f = open('cipher1.txt', 'r')
l = f.readlines()
f.close()
ln = l[0].strip()
cl = ln.split(',')

abl = list(range(ord('a'), ord('z')+1))
kl = []
for i in abl:
    for j in abl:
        for k in abl:
            kl.append(d2b(i)+d2b(j)+d2b(k))

ab = list(range(ord('a'), ord('z')+1))+list(range(ord('A'), ord('Z')+1))+list(range(ord('0'), ord(';')+1))+[ord(','), ord('.'), ord('-'), ord('('), ord(')'), ord('!'), ord('?'), ord("'"), ord(' ')]

i = 0
j = 0
while((j < len(cl))and(i < len(kl))):
    j = 0
    keyl = [kl[i][:8], kl[i][8:16], kl[i][16:]]
    res = []
    r = 100
    while(((r in ab))and(j < len(cl))):
        s = int(cl[j])
        r = s ^ int(keyl[j%3], 2)
        if(r in ab):
            res.append(r)
        j = j + 1
    i = i + 1
print(i, j, sum(res))
