# Description of the problem can be found at http://codeforces.com/problemset/problem/92/A

import math

n, m = map(int, input().split())

m -= (2*m // (n * (n + 1))) * (n * (n + 1)) // 2

x = (-1 + math.sqrt(1 + 4*2*m)) // 2

print(int(m - (x*(x + 1)) // 2))