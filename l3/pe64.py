"""
All square roots are periodic when written as continued fractions and can be written in the form:
√N = a_(0) + 	
1
  	a_(1) + 	
1
  	  	a_(2) + 	
1
  	  	  	a_(3) + ...

For example, let us consider √23:
√23 = 4 + √23 — 4 = 4 +  	
1
	 = 4 +  	
1
  	
1
√23—4
	  	1 +  	
√23 – 3
7

If we continue we would get the following expansion:
√23 = 4 + 	
1
  	1 + 	
1
  	  	3 + 	
1
  	  	  	1 + 	
1
  	  	  	  	8 + ...

The process can be summarised as follows:
a_(0) = 4, 	  	
1
√23—4
	 =  	
√23+4
7
	 = 1 +  	
√23—3
7
a_(1) = 1, 	  	
7
√23—3
	 =  	
7(√23+3)
14
	 = 3 +  	
√23—3
2
a_(2) = 3, 	  	
2
√23—3
	 =  	
2(√23+3)
14
	 = 1 +  	
√23—4
7
a_(3) = 1, 	  	
7
√23—4
	 =  	
7(√23+4)
7
	 = 8 +  	√23—4
a_(4) = 8, 	  	
1
√23—4
	 =  	
√23+4
7
	 = 1 +  	
√23—3
7
a_(5) = 1, 	  	
7
√23—3
	 =  	
7(√23+3)
14
	 = 3 +  	
√23—3
2
a_(6) = 3, 	  	
2
√23—3
	 =  	
2(√23+3)
14
	 = 1 +  	
√23—4
7
a_(7) = 1, 	  	
7
√23—4
	 =  	
7(√23+4)
7
	 = 8 +  	√23—4

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

import math

def isSquare(n):
    r = math.sqrt(n)
    return(int(r) == r)

def step(n):
    rn = [] + n
    if(0 == rn[0]):
        while(math.sqrt(rn[2]) + rn[3] <= 0):
            rn[0] = rn[0] - 1
            rn[3] = rn[3] + rn[1]
        if(rn[1] > 1):
            while(math.sqrt(rn[2]) + rn[3] >= rn[1]):
                rn[0] = rn[0] + 1
                rn[3] = rn[3] - rn[1]
        else:
            rn[0] = rn[3]
            rn[3] = -math.floor(math.sqrt(rn[2]))
            rn[0] = rn[0] - rn[3]
    else:
        newD = (rn[2] - rn[3]**2) / rn[1]
        if(0 == newD - int(newD)):
            rn = [0, int(newD), rn[2], -rn[3]]
        else:
            rn = []
    return rn

N = 10000
c = 0
for i in range(2, N+1):
    if(not(isSquare(i))):
        n = [0, 1, i, 0]
        nl = []
        while(not(n in nl)):
            if(0 != n[0]):
                nl.append(n)
            n = step(n)
        c = (len(nl)-1) % 2 + c
print(c)
