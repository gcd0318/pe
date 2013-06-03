"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import math

def sumOfDiag(m):
    res = 0
    for i in range(0, len(m)):
        res = res + m[i][i] + m[i][-1-i]
    return(res - 1)

def upright(n):
    return((2*n+1)**2)
def upleft(n):
    return((2*n)**2 - (2*n-1))
def downright(n):
    return((2*n+1)**2-(2*n))
def downleft(n):
    return((2*n)**2+1)


#m=[[21,22,23,24,25],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]]

c = math.floor(1001/2)

tot = 0
for i in range(1, int(1001/2)+1):
    tot = tot+upright(i)+upleft(i)+downright(i)+downleft(i)
tot = tot + 1

print(int(1+(2/3)*c*(13+c*(15+8*c))))
print (tot)
