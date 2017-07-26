# Description of the problem can be found at http://codeforces.com/problemset/problem/614/A

import math

l, r, k = map(int, input().split())

x = 0
l_a = list()
while True:
    a = k ** x
    if a >= l and a <= r:
        l_a.append(a)
    elif a >= r:
        break
    x += 1

if len(l_a) == 0:
    print(-1)
else:
    print(" ".join(str(x) for x in l_a))