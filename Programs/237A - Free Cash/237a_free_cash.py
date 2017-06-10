# Description of the problem can be found at http://codeforces.com/problemset/problem/237/A

n = int(input())

p_h = -1
p_m = -1
m_c = 0
c = 0

for _ in range(n):
    h, m = map(int, input().split())
    
    if h == p_h and m == p_m:
        c += 1
    else:
        c = 1
    if c > m_c:
        m_c = c
    p_h, p_m = h, m

print(m_c)