# Description of the problem can be found at http://codeforces.com/problemset/problem/519/C

n, m = map(int, input().split())
m_t = 0

for i in range(0, min(n, m // 2 ) + 1):
    t_2 = min((n - i) // 2, m - i * 2)
    m_t = max(m_t, t_2 + i)
print(m_t)