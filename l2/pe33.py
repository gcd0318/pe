"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def equal(c1, c2):
    return(c1[0]*c2[1] == c1[1]*c2[0])

def gcd(a, b):
    if (a > b):
        a = a + b
        b = a - b
        a = a - b
    r = b % a
    if(0 == r):
        return a
    else:
        return(gcd(r, a))

def lct(m, d):
    g = gcd(m, d)
    if(1 != g):
        m = int(m/g)
        d = int(d/g)
    return([m, d])

def noc(s1, s2):
    i = 0
    for s in s1:
        if(s in s2):
            i = i + 1
    return i

print(gcd(20,40))


resn = 1
resd = 1
for n in range(10, 100):
    for d in range(n+1, 100):
        if(0 != gcd(n, d)%10):
            sn = str(n)
            sd = str(d)
            if(1 == noc(sn, sd)):
                for s in sn:
                    if(s in sd):
                        sn = sn.replace(s, '', 1)
                        sd = sd.replace(s, '', 1)
                if(equal([n, d], [int(sn), int(sd)])):
                    c = lct(n, d)
                    resn = resn * n
                    resd = resd* d
                    print(n, d, c)

print(lct(resn, resd))
