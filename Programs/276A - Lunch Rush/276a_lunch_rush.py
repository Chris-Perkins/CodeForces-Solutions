# Description of the problem can be found at http://codeforces.com/problemset/problem/276/A

n, k = map(int, input().split())

m_j = -1e10
for _ in range(n):
    f, t = map(int, input().split())
    m_j = max(f - max(0, t - k), m_j)
print(m_j)