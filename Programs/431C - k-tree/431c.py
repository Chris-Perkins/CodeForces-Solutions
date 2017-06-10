# Description of the problem can be found at http://codeforces.com/problemset/problem/431/C

n, k, d = map(int, input().split())
f = [0] * (n + 1)
g = [1] * (n + 1)
d = 1 - d
m = 1000000007
for i in range(1, n + 1):
    f[i] = (sum(g[j] for j in range(max(0, i - k), d + i)) + sum(f[j] for j in range(max(0, d + i), i))) % m
    g[i] = sum(g[j] for j in range(max(0, i - k), i)) % m
print(f[n])