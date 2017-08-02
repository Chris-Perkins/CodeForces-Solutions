# Description of the problem can be found at http://codeforces.com/problemset/problem/168/A

import math

n, x, y = map(int, input().split())

print(max(0, math.ceil((n * y) / 100) - x))