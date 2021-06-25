"""
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.
"""

B = 10 ** 10

def top_n_primes(n, primes=[2]):
    if (0 < n):
        ins = 2
#        primes = [2]
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

def nth_prime(n, primes=[2]):
    res = 0
    if (0 < n):
        res = top_n_primes(n, primes)[-1]
    return res

# print(nth_prime(7037))

def r(n, primes=[2]):
    res = 2
    if 0 != n % 2:
        p = nth_prime(n, primes)
        if 2 * n < p:
            res = 2 * n * p
        else:
            res = (2 * n * p) % (p * p)
    return res


n = 7037
primes = top_n_primes(n)
print(primes[-1])
print(r(7036, primes))
print(r(7037, primes))
while primes[-1] < 10 ** 5:
    n = n + 2
    primes = top_n_primes(n, primes)

print(n)
print(primes[-1])

while r(n, primes) < B:
    print(n)
    n = n + 2
print(primes)
print(n)
