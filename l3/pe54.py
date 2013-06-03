"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card. 
One Pair: Two cards of the same value. 
Two Pairs: Two different pairs. 
Three of a Kind: Three cards of the same value. 
Straight: All cards are consecutive values. 
Flush: All cards of the same suit. 
Full House: Three of a kind and a pair. 
Four of a Kind: Four cards of the same value. 
Straight Flush: All cards are consecutive values of same suit. 
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. 
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand   Player 1   Player 2   Winner 
1   5H 5C 6S 7S KD

Pair of Fives   2C 3S 8S 8D TD

Pair of Eights   Player 2 
2   5D 8C 9S JS AC

Highest card Ace   2C 5C 7D 8S QH

Highest card Queen   Player 1 
3   2D 9C AS AH AC

Three Aces   3D 6D 7D TD QD

Flush with Diamonds   Player 2 
4   4D 6S 9H QH QC

Pair of Queens
Highest card Nine   3D 6D 7H QD QS

Pair of Queens
Highest card Seven   Player 1 
5   2H 2D 4C 4D 4S

Full House
With Three Fours   3C 3D 3S 9S 9D

Full House
with Three Threes   Player 1 

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

def value(x):
    if('T' == x):
        return 10
    elif('J' == x):
        return 11
    elif('Q' == x):
        return 12
    elif('K' == x):
        return 13
    elif('A' == x):
        return 14
    else:
        return(int(x))

def cont(l):
    i = 1
    res = True
    tl = l + []
    tl.sort()
    while(res and(i < len(tl))):
        res = res and(1 == tl[i]-tl[i-1])
        i = i + 1
    return res

def kvvk(d):
    resd = {}
    for i in d.keys():
        for j in d[i]:
            if(j in resd.keys()):
                resd[j].append(i)
            else:
                resd[j] = [i]
    return resd

def rank(kvd):
    vkd = kvvk(kvd)
    samevaluedict = {}
    for i in range(1, 4+1):
        samevaluedict[i] = 0
    for i in vkd:
        ind = len(vkd[i])
        samevaluedict[ind] = samevaluedict[ind] + 1
    vl = []
    for i in kvd.keys():
        vl = vl + kvd[i]
    vl.sort()
    vl.reverse()
    if(1 == len(kvd)):
        if(cont(vl)):
            if(14 == max(vl)):
                return([9])
            else:
                return([8]+vl)
        else:
            return([5]+vl)
    elif(1 == samevaluedict[4]):
        i = 0
        tl = list(vkd.keys())
        while((4 != len(vkd[tl[i]]))and(i < len(vkd.keys()))):
            i = i + 1
        rl0 = tl[i]
        rl1 = sum(tl) - rl0
        return([7, rl0, rl1])
    elif(1 == samevaluedict[3]):
        i = 0
        tl = list(vkd.keys())
        while((3 != len(vkd[tl[i]]))and(i < len(vkd.keys()))):
            i = i + 1
        rl0 = tl[i]
        if(1 == samevaluedict[2]):
            rl1 = sum(tl) - rl0
            return([6, rl0, rl1])
        else:
            l = tl + []
            l.remove(rl0)
            l.sort()
            l.reverse()
            return([3, rl0]+l)
    elif(5 == (len(vl))and(cont(vl))):
        return [4, max(list(vkd.keys()))]
    elif(2 == samevaluedict[2]):
        tl = list(vkd.keys())
        tl.sort()
        tl.reverse()
        l = []
        for t in tl:
            if(2 == len(vkd[t])):
                l.append(t)
        l.sort()
        l.reverse()
        for t in vl:
            if(not(t in l)):
                l.append(t)
        return([2]+l)
    elif((1 == samevaluedict[2])and(0 == samevaluedict[3])):
        tl = list(vkd.keys())
        tl.sort()
        tl.reverse()
        l = []
        for t in tl:
            if(2 == len(vkd[t])):
                l.append(t)
        l.sort()
        l.reverse()
        for t in vl:
            if(not(t in l)):
                l.append(t)
        return([1]+l)
    elif((not(cont(list(vkd.keys()))))and(5 == samevaluedict[1])):
        return([0]+vl)
    else:
        return None

def getBiggerList1(l1, l2):
    if(len(l1) <= len(l2)):
        i = 0
        while(i < len(l1))and(l1[i] == l2[i]):
            i = i + 1
        if(i > len(l1)):
            if(len(l1) == len(l2)):
                return l1
            else:
                return l2
        else:
            if(l1[i] > l2[i]):
                return l1
            else:
                return l2
    else:
        return(getBiggerList(l2, l1))

def getBiggerList(l1, l2):
    if(len(l1) > len(l2)):
        return(getBiggerList(l2, l1))
    else:
        if(0 == len(l1)):
            if(0 == len(l2)):
                return l1
            else:
                return l2
        else:
            if(l1[0] == l2[0]):
                return([l1[0]]+getBiggerList(l1[1:], l2[1:]))
            else:
                if(l1[0] < l2[0]):
                    return(l2)
                else:
                    return(l1)

def winner(d1, d2):
    r1 = rank(d1)
    r2 = rank(d2)
    if(getBiggerList(r1, r2) == r1):
        return d1
    else:
        return d2

f = open('poker.txt', 'r')
l = f.readlines()
f.close()
win = 0

for gl in l:
    gl = gl.strip()
    tl = gl.split(' ')
    d1 = {}
    d2 = {}
    for i in range(0, 4+1):
        k = tl[i][1]
        if(k in d1.keys()):
            d1[k].append(value(tl[i][0]))
        else:
            d1[k] = [value(tl[i][0])]
    for i in range(5, 9+1):
        k = tl[i][1]
        if(k in d2.keys()):
            d2[k].append(value(tl[i][0]))
        else:
            d2[k] = [value(tl[i][0])]
    if(winner(d1,d2)==d1):
        win = win + 1
print(win)
