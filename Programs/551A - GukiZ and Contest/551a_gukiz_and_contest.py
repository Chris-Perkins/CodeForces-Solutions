# Description of the problem can be found at http://codeforces.com/problemset/problem/551/A

n = int(input())
l_r = list(map(int, input().split()))
l_r_c = list(l_r)
l_r_c.sort(reverse = True)
d = {}

t = 1
for r in l_r_c:
    if r not in d:
        d[r] = t
    t += 1

for r in l_r:
    print(d[r], end = " ")