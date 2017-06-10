# Description of the problem can be found at http://codeforces.com/problemset/problem/789/A

import math

n, k = map(int, input().split())

l_p = list(map(int, input().split()))

t = 0

for p in l_p:
    t += math.ceil(p / k)

print(math.ceil(t / 2))