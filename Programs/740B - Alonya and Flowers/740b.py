# Description of the problem can be found at http://codeforces.com/problemset/problem/740/B

n, m = map(int, input().split())
l_v = list([0])
l_v.extend((map(int, input().split())))
s_v = [0] * (n + 1)

for i in range(1, n + 1):
    s_v[i] += s_v[i - 1] + l_v[i]

t = 0
for _ in range(m):
    l, r = map(int, input().split())
    if s_v[r] - s_v[l - 1] > 0:
        t += s_v[r] - s_v[l - 1]

print(t)