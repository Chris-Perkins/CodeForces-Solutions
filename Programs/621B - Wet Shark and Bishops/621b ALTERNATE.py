# Description of the problem can be found at http://codeforces.com/problemset/problem/621/B

d_p = {}
d_s = {}

n_p = int(input())
t = 0

for i in range(n_p):
    x, y = map(int, input().split())
    a = x + y
    s = x - y
    if a not in d_p:
        d_p[a] = 0
    if s not in d_s:
        d_s[s] = 0
    d_p[a] += 1
    d_s[s] += 1
    
    t += d_p[a] - 1
    t += d_s[s] - 1

print(t)