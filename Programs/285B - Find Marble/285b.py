# Description of the problem can be found at http://codeforces.com/problemset/problem/285/B

n, s, t = map(int, input().split())
l_m = list(map(int, input().split()))

o_s = s
m_c = 0
while s != t:
    s = l_m[s - 1]
    m_c += 1
    
    if s == o_s:
        m_c = -1
        break
    
print(m_c)