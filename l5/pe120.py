"""
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
"""

def maxr(a):
    return max(2, 2 * a * ((a - 1) // 2))

print(maxr(7))

T = 1000

sr = 0
for i in range(3, T + 1):
    sr = sr + maxr(i)
print(sr)

