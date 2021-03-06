"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to problems 105 and 106.
"""

def subsets(s):
    res = []
    tmp = [s]
    while(0 < len(tmp)):
        ts = tmp.pop()
        if(not ts in res):
            res.append(ts)
        if(0 < len(ts)):
            for i in range(len(ts)):
                tmp.append(ts[:i]+ts[i+1:])
    
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
                if(0<len(s1)*len(s2))and(is_disjoint(s1, s2)):
#                    print(s1, sum(s1), s2, sum(s2))
                    res = (sum(s1)!=sum(s2))and((sum(s1)-sum(s2))*(len(s1)-len(s2))>=0)and res
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

s_i = [11,18,19,20,22,25]
s = ''
for e in gen_from_seed(s_i):
    s = s+str(e)
print(s)
