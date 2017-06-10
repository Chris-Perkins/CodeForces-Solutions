# Description of the problem can be found at http://codeforces.com/problemset/problem/670/B

import math

n, k = map(int, input().split())
l_i = list(map(int, input().split()))

x = int((-1 + math.sqrt(1 + 4 * 2 * k)) // 2)

if (x ** 2 + x) // 2 == k:
    print(l_i[x - 1])
else:
    print(l_i[k - (x**2 + x) // 2 - 1])