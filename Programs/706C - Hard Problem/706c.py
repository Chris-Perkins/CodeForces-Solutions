# Description of the problem can be found at 

import sys

n = int(input())
c = [int(x) for x in input().split()]
s = [x.strip() for x in sys.stdin.readlines()]
r = [x[::-1] for x in s]

h = [[None, None] for _ in range(n)]

h[0][0] = 0
h[0][1] = c[0]

for i in range(1, n):
    p, q = s[i], s[i][::-1]
    if s[i-1] <= p and h[i-1][0] is not None:
        h[i][0] = h[i-1][0]
    if r[i-1] <= p:
        if h[i-1][1] is not None and (h[i][0] is None or h[i][0] > h[i-1][1]):
            h[i][0] = h[i-1][1]
    if s[i-1] <= q and h[i-1][0] is not None:
        h[i][1] = h[i-1][0] + c[i]
    if r[i-1] <= q:
        if h[i-1][1] is not None and (h[i][1] is None or h[i][1] > h[i-1][1] + c[i]):
            h[i][1] = h[i-1][1] + c[i]

p, q = h[n-1][0], h[n-1][1]
if p is not None and q is not None:
    print(min(p, q))
elif p is not None:
    print(p)
elif q is not None:
    print(q)
else:
    print(-1)