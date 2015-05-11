"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.
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

f = open("p105_sets.txt", "r")
ls = f.readlines()
f.close()
sets = []
for l in ls:
    tset = []
    ess = l.split(',')
    for es in ess:
        tset.append(int(es))
    sets.append(tset)

ress = []
i = 0
for s in sets:
    i = i + 1
    if(is_sss(s)):
        ress.append(sum(s))
print(sum(ress))
