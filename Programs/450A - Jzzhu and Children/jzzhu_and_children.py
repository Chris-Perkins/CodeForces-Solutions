# Description of the problem can be found at http://codeforces.com/problemset/problem/450/A

n, m = map(int, input().split())

m_i = -1
m_t = -1

i = 0
for c in list(map(int, input().split())):
    n_t = c // m + (0 if c % m == 0 else 1)
    if n_t >= m_t:
        m_t = n_t
        m_i = i
    i += 1
    
print(m_i + 1)