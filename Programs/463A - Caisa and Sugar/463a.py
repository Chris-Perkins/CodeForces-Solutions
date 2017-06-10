# Description of the problem can be found at http://codeforces.com/problemset/problem/463/A

n, s = map(int, input().split())

m = -1
for _ in range(n):
    d, c = map(int, input().split())
    if s > d or (s == d and c == 0):
        m = max(m, (100 - c) % 100)

print(int(m))