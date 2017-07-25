# Description of the problem can be found at http://codeforces.com/problemset/problem/157/B

import math

n = int(input())
l_s = list(map(int, input().split()))
l_s.sort(reverse = True)

t = 0
for index in range(n):
    t += (-1 if index % 2 == 1 else 1) * l_s[index] ** 2

print(t * math.pi)