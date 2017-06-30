# Description of the problem can be found at http://codeforces.com/problemset/problem/558/B

n = int(input())
l_i = list(map(int, input().split()))

d = {}
m_b = 0
m_b_i = 0
m_l = 0

for i in range(n):
    if l_i[i] not in d:
        d[l_i[i]] = [0, i]
    d[l_i[i]][0] += 1
    
    if d[l_i[i]][0] > m_b:
        m_b = d[l_i[i]][0]
        m_b_i = i
        m_l = i - d[l_i[i]][1]
    elif d[l_i[i]][0] == m_b and i - d[l_i[i]][1] < m_l:
        m_b = d[l_i[i]][0]
        m_b_i = i
        m_l = i - d[l_i[i]][1]

print(d[l_i[m_b_i]][1] + 1, m_b_i + 1)