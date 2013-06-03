"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

import math

res = str(int(math.pow(2, 1000)))
sum = 0
for i in res:
    sum = sum + int(i)
print (sum)
