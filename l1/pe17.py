"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 



NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import math

def numToName(n):
    l = {1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine',
         10:'ten',
         11:'eleven',
         12:'twelve',
         13:'thirteen',
         14:'fourteen',
         15:'fifteen',
         16:'sixteen',
         17:'seventeen',
         18:'eighteen',
         19:'nineteen',
         20:'twenty',
         30:'thirty',
         40:'forty',
         50:'fifty',
         60:'sixty',
         70:'seventy',
         80:'eighty',
         90:'ninety',
         100:'hundred',
         1000:'thousand'}
    if (20 >= n):
        return l[n]
    elif(100 > n):
        d = l[math.floor(n/10)*10]
        if (0 == n%10):
            s = ''
        else:
            s = l[n%10]
        return (d+s)
    elif(1000 > n):
        if (0 == n%100):
            return (l[math.floor(n/100)]+l[100])
        else:
            return (l[math.floor(n/100)]+l[100]+'and'+numToName(n%100))
    elif(1000 == n):
        return (l[1]+l[1000])
    else:
        return ''



n = 1000
s = ''

for i in range(1, n+1):
    s = s + numToName(i)
print (len(s))
