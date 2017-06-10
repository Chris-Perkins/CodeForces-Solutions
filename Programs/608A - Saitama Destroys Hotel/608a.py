# Description of the problem can be found at http://codeforces.com/problemset/problem/608/A

n, t = map(int, input().split())

m_t = 0
for _ in range(n):
    f, t_f = map(int, input().split())
    m_t = max(m_t, t + max(0, t_f - t + f))
print(m_t)