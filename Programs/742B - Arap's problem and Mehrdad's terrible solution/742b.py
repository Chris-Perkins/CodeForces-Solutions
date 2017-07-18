# Description of the problem can be found at http://codeforces.com/problemset/problem/742/B

_, X = map(int, input().split())
l_n = list(map(int, input().split()))

d = {}
t = 0
for n in l_n:
    if n^X in d:
        t += d[n ^ X]
    if n not in d:
        d[n] = 0
    d[n] += 1
print(t)