# Description of the problem can be found at http://codeforces.com/problemset/problem/385/A

n, c = map(int, input().split())
l_p = list(map(int, input().split()))

m = 0

for i in range(n - 1):
    m = max(l_p[i] - l_p[i + 1] - c, m)

print(m)