# Description of the problem can be found at http://codeforces.com/problemset/problem/680/A

l_n = list(map(int, input().split()))

d_n = {}
m = 0

for n in l_n:
    if n not in d_n:
        d_n[n] = 1
    else:
        d_n[n] += 1
    if d_n[n] >= 2 and d_n[n] <= 3:
        m = max(m, d_n[n] * n)
print(sum(l_n) - m)