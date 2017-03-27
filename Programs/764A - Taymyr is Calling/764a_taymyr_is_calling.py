# Description of the problem can be found at http://codeforces.com/problemset/problem/764/A

n, m, z = map(int, input().split())
t = 0

for i in range(1, z // m + 1):
    if (i * m) % n == 0:
        t += 1
print(t)