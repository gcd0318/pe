"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def d2b(n):
    if(1 >= n):
        return n
    else:
        return(int(str(d2b(int(n/2)))+str(n%2)))

def isPalindromic(s):
    if(1 >= len(s)):
        return True
    else:
        return((s[0]==s[-1])and isPalindromic(s[1:-1]))

res = 0
for i in range(1, 1000000+1):
    if((isPalindromic(str(i)))and(isPalindromic(str(d2b(i))))):
        print(i, d2b(i))
        res = res + i
print(res)
