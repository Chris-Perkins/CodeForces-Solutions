# Description of the problem can be found at http://codeforces.com/problemset/problem/570/A

n, m = map(int, input().split())
t = [0] * (n + 1)

m_v_t = -1

for _ in range(m):
    m_i_c = -1
    m_v_c = -1
    
    l_v = list(map(int, input().split()))
    
    for i in range(1, n + 1):
        if l_v[i - 1] > m_v_c:
            m_i_c = i
            m_v_c = l_v[i - 1]
    
    t[m_i_c] += 1
    
    if t[m_i_c] > m_v_t:
        m_v_t = t[m_i_c]

for i in range(len(t)):
    if t[i] == m_v_t:
        print(i)
        quit()