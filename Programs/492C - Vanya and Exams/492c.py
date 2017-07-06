# Description of the problem can be found at http://codeforces.com/problemset/problem/492/C

n, r, avg = map(int, input().split())

t = 0
s = 0
l_s = list()
for _ in range(n):
    a, b = map(int, input().split())
    s += a
    l_s.append([a, b])

l_s.sort(key = lambda x: x[1])
i = 0
while s / n < avg:
    t += min(r - l_s[i][0], n * avg - s) * l_s[i][1]
    s += min(r - l_s[i][0], n * avg - s)
    i += 1

print(t)
    