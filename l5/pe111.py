'''
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d	M(4, d)	N(4, d)	S(4, d)
0	2	13	67061
1	3	9	22275
2	3	1	2221
3	3	12	46214
4	3	2	8888
5	3	1	5557
6	3	1	6661
7	3	9	57863
8	3	1	8887
9	3	7	48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
'''

import math

def lessPrime(n):
    res = []
    l = [0,0]
    for i in range(2, n+1):
        l.append(i)
    m = len(l)//2 + 1
    i = 2
    while(i <= m):
        while (0 != l[i]):
            t = i * 2
            while (t < len(l)):
                l[t] = 0
                t = t + i
            i = i + 1
        i = i + 1
    for i in l:
        if(0 != i):
            res.append(i)
    return res

def intoPrime(n):
    half = math.floor(math.sqrt(n))
    l = [0, 0]
    for i in range(2, half+1):
        l.append(i)
    i = 0
    while (i < len(l)):
        t = i
        if (0 != l[i]):
            while(t + i < len(l)):
                t = t + i
                l[t] = 0
        i = i + 1
    i = 0
    while((0 < len(l)) and ((0 == i) or (0 != n % i))):
        i = l.pop()
        if (0 != i):
            if (0 == n % i):
                return [i] + intoPrime(n//i)
    return [n]

def prime_rate(x):
    d = {}
    if(1 < x):
        l = intoPrime(x)
        for i in l:
            d[i] = 0
        for i in l:
            r = 0
            t = x
            while(0 == t % i):
                r = r + 1
                t = t // i
            d[i] = r
    return d

def top_n_primes(n):
    primes = []
    if (0 < n):
        ins = 2
        primes = [2]
        while(len(primes) < n):
            ins = ins + 1
            devided = False
            i = 0
            while not(devided) and (i < len(primes)):
                devided = (0 == ins % primes[i])
                i = i + 1
            if not devided:
                primes.append(ins)
    return primes

def nth_prime(n):
    res = 0
    if (0 < n):
        res = top_n_primes(n)[-1]
    return res

def mul(l):
    res = 1
    for i in l:
        res = res * i
    return res

def isPrime(n):
    l = [0,0]
    if(2 > n):
        return None
    else:
        for i in range(2, n+1):
            l.append(i)
        for i in l:
            t = i
            if(0 != l[i]):
                t = t + i
                while(t < len(l)):
                    l[t] = 0
                    t = t + i
    return(0 != l[n])

def between_primes(s, e):
	resl = []
	for i in lessPrime(e):
		if i >=s:
			resl.append(i)
	return resl

def into_digits(n):
	resl = []
	for c in str(n):
		resl.append(c)
	return resl

def get(num):
	l = between_primes(10**(num-1), 10**num-1)
	print(len(l))
#	resd = {}
	res = 0
	for d in range(10):
		rd = {}
		for i in l:
			k = str(i).count(str(d))
			if k in rd:
				rd[k].append(i)
			else:
				rd[k] = [i]
		m = max(rd.keys())
#		n = len(rd[m])
		s = sum(rd[m])
		resd[d] = [m, n, s]
#		res = res + s
	return resd

print(lessPrime(100))


r = get(10)
print(r)
