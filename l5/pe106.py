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
#        print(res)
#        print('-----------------------')
#        print(tmp)
#        print('====================')
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


