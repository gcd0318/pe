"""


The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""
"""

How do you read and write Roman numerals?

Traditional Roman numerals are made up of the following denominations:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

You will read about many different rules concerning Roman numerals, but the truth is that the Romans only had one simple rule:

Numerals must be arranged in descending order of size.

For example, three ways that sixteen could be written are XVI, XIIIIII, VVVI; the first being the preferred form as it uses the least number of numerals.

The "descending size" rule was introduced to allow the use of subtractive combinations. For example, four can be written IV because it is one before five. As the rule requires that the numerals be arranged in order of size it should be clear to a reader that the presence of a smaller numeral out of place, so to speak, was unambiguously to be subtracted from the following numeral. For example, nineteen could be written XIX = X + IX (9). Note also how the rule requires X (ten) be placed before IX (nine), and IXX would not be an acceptable configuration.

Generally the Romans tried to use as few numerals as possible when displaying numbers. For this reason, XIX would be the preferred form of nineteen over other valid combinations, like XVIIII or XVIV. However, this was NOT a rule and there still remain in Rome many examples where economy of numerals has not been employed. For example, in the famous Colesseum the the numerals above the forty-ninth entrance is written XXXXVIIII and not IL nor XLIX (see rules below).

Despite this, over time we have continued to introduce new restrictive rules. By mediaeval times it had become standard practice to avoid more than three consecutive identical numerals. That is, IV would be written instead of IIII, IX would be used instead of VIIII, and so on. In addition, the subtractive combinations had the following rules superimposed:

    Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
    I can only be placed before V and X.
    X can only be placed before L and C.
    C can only be placed before D and M.

These last four rules are considered to be law, and generally it is preferred, but not necessary, to display numbers using the minimum number of numerals. Which means that IL is considered an invalid way of writing forty-nine, and whereas XXXXVIIII, XXXXIX, XLVIIII, and XLIX are all quite legitimate, the latter is the preferred (minimal) form.

It is also expected that higher denominations should be used whenever possible; for example, L should be used in place of XXXXX, or C should be used in place of LL. However, even this "rule" has been flaunted: in the church of Sant'Agnese fuori le Mura (St Agnes' outside the walls), found in Rome, the date, MCCCCCCVI (1606), is written on the gilded and coffered wooden ceiling; I am sure that many would argue that it should have been written MDCVI.

However, if we believe the adage, "when in Rome do as the Romans do," and we see how the Romans write numerals, then it clearly gives us much more freedom than many would care to admit.
"""


d1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
sub = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
ds = {}
for s in sub:
    ds[s] = d1[s[1]] - d1[s[0]]

def r2d(r):
    res = 0
    i = 0
    while(i < len(sub)):
        s = sub[i]
        i = i + 1
        if s in r:
            i = len(sub) + 1
            rs = r.split(s, 1)
            res = ds[s] + r2d(rs[0]) + r2d(rs[1])
    if(i == len(sub)):
        for c in r:
            res = res + d1[c]
    return res

d2 = {}
for k in d1:
    d2[d1[k]] = k
for k in ds:
    d2[ds[k]] = k
#d2[5000]='G'
#d2[4000]='MG'
#print(d2)
def d2r(d):
    res = ''
    kls = list(d2.keys())
    kls.sort(reverse = True)
    for n in kls:
        while(d >= n):
            res = res + d2[n]
            d = d - n
    return res

f = open('roman.txt', 'r')
ls = f.readlines()
f.close

res = 0
rr = 0
for l in ls:
    l = l.strip()
    res = res + len(d2r(r2d(l)))
    rr = rr + len(l)
print(rr - res)


"""

How do you read and write Roman numerals?

Traditional Roman numerals are made up of the following denominations:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

You will read about many different rules concerning Roman numerals, but the truth is that the Romans only had one simple rule:

Numerals must be arranged in descending order of size.

For example, three ways that sixteen could be written are XVI, XIIIIII, VVVI; the first being the preferred form as it uses the least number of numerals.

The "descending size" rule was introduced to allow the use of subtractive combinations. For example, four can be written IV because it is one before five. As the rule requires that the numerals be arranged in order of size it should be clear to a reader that the presence of a smaller numeral out of place, so to speak, was unambiguously to be subtracted from the following numeral. For example, nineteen could be written XIX = X + IX (9). Note also how the rule requires X (ten) be placed before IX (nine), and IXX would not be an acceptable configuration.

Generally the Romans tried to use as few numerals as possible when displaying numbers. For this reason, XIX would be the preferred form of nineteen over other valid combinations, like XVIIII or XVIV. However, this was NOT a rule and there still remain in Rome many examples where economy of numerals has not been employed. For example, in the famous Colesseum the the numerals above the forty-ninth entrance is written XXXXVIIII and not IL nor XLIX (see rules below).

Despite this, over time we have continued to introduce new restrictive rules. By mediaeval times it had become standard practice to avoid more than three consecutive identical numerals. That is, IV would be written instead of IIII, IX would be used instead of VIIII, and so on. In addition, the subtractive combinations had the following rules superimposed:

    Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
    I can only be placed before V and X.
    X can only be placed before L and C.
    C can only be placed before D and M.

These last four rules are considered to be law, and generally it is preferred, but not necessary, to display numbers using the minimum number of numerals. Which means that IL is considered an invalid way of writing forty-nine, and whereas XXXXVIIII, XXXXIX, XLVIIII, and XLIX are all quite legitimate, the latter is the preferred (minimal) form.

It is also expected that higher denominations should be used whenever possible; for example, L should be used in place of XXXXX, or C should be used in place of LL. However, even this "rule" has been flaunted: in the church of Sant'Agnese fuori le Mura (St Agnes' outside the walls), found in Rome, the date, MCCCCCCVI (1606), is written on the gilded and coffered wooden ceiling; I am sure that many would argue that it should have been written MDCVI.

However, if we believe the adage, "when in Rome do as the Romans do," and we see how the Romans write numerals, then it clearly gives us much more freedom than many would care to admit.
"""
