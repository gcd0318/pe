"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.
"""


def subsets(s):
    s.sort()
    res = []
    tmp = [s+[]]
    while(0 < len(tmp)):
        ts = tmp.pop()
        if(not ts in res):
            res.append(ts+[])
        if(0 < len(ts)):
            for i in range(len(ts)):
                aset = ts[:i]+ts[i+1:]
                aset.sort()
                tmp.append(aset+[])
    return res

def sumup(s):
    res = 0
    if(0 < len(s)):
        res = sum(s)
    return res

def is_disjoint(s1, s2):
    if(len(s1) > len(s2)):
        return is_disjoint(s2, s1)
    res = True
    i = 0
    while(res and (i<len(s1))):
        res = not(s1[i] in s2)
        i = i + 1
    return res

def is_sss(s):
    res = True
    if(1 < len(s)):
        ss = subsets(s)
        i = 0
        while(i < len(ss) and res):
            s1 = ss[i]
            j = i + 1
            while(j < len(ss) and res):
                s2 = ss[j]
#                print(s1, sum(s1), s2, sum(s2))
                l1 = len(s1)
                l2 = len(s2)
                ss1 = sum(s1)
                ss2 = sum(s2)
                if(0<l1)and(0<l2)and(is_disjoint(s1, s2)):
#                    print(s1, sum(s1), s2, sum(s2))
                    res = (ss1!=ss2)and((l1==l2)or((ss1-ss2>0)==(l1-l2>0)))and res
#                    print(res)
                j = j + 1
            i = i + 1
    return res

def gen_from_seed(seed):
    res = []
    mid = seed[len(seed)//2]
    res.append(mid)
    for e in seed:
        res.append(mid+e)
    res.sort()
    return res

def equ_subset_pairs(s):
    resl = []
    ssets = subsets(s)
    for i in range(len(ssets)):
        for j in range(i, len(ssets)):
            subset1 = ssets[i]
            subset2 = ssets[j]
            if(subset1 and subset2) and is_disjoint(subset1, subset2):# and (len(subset1) == len(subset2)) or (0 < ((len(subset1) - len(subset2)) * (sumup(subset1) - sumup(subset2))))):
                if((len(subset1) < len(subset2))):
                    resl.append((subset2, subset1))
                else:
                    resl.append((subset1, subset2))
    return resl

def equ_subset_pairs(s):
    resl = []
    ssets = subsets(s)
    for i in range(len(ssets)):
        for j in range(i, len(ssets)):
            subset1 = ssets[i]
            subset2 = ssets[j]
            if(subset1 and subset2) and is_disjoint(subset1, subset2) and (len(subset1) == len(subset2)):# or (0 < ((len(subset1) - len(subset2)) * (sumup(subset1) - sumup(subset2))))):
                if((len(subset1) < len(subset2))):
                    resl.append((subset2, subset1))
                else:
                    resl.append((subset1, subset2))
    return resl

def sign(n):
    res = n
    if (n < 0):
        res = -1
    elif (0 < n):
        res = 1
    return res

def s_comp(s1, s2):
    res = True
    i = 0
    while res and (i < len(s1)):
        res = res and (0 <= (s1[i]-s2[i])*(s1[0]-s2[0]))
        i = i + 1
    return res



def sub_i(n, k):
    res = []
    if (1 == k):
        for i in range(n):
            res.append([i])
    elif(1 < k):
        for si in sub_i(n, k-1):
            m = max(si)
            while m < n-1:
                res.append(si+[m+1])
                m = m + 1
    return res

def sub_s(s, k):
    res = []
    for si in sub_i(len(s), k):
        res.append([s[i] for i in si])
    return res


#s = [3,5,6,7]
#s = [20,31,38,39,40,42,45]
#s = [1,2,3,4]
s = list(range(12))
#sps = equ_subset_pairs(s)
#print(len(sps))
#for p in sps:
#    print(p)

i = 0
#for p in sps:
#    if(len(p[0]) == len(p[1])) and (not s_comp(p[0], p[1])):
#        i = i + 1
#        print(p, sumup(p[0]), sumup(p[1]))

for n in range(2, len(s)):
    subs = sub_s(s, n)
    print(n, len(subs))
    for j in range(len(subs)):
        for k in range(j, len(subs)):
            if (not s_comp(subs[j], subs[k])) and (is_disjoint(subs[j], subs[k])):
#                print(subs[j], subs[k])
                i = i + 1
#        print(i, j, k)
#    print(i, j, k)
print(i)