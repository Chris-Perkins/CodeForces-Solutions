# Description of the problem can be found at http://codeforces.com/problemset/problem/699/A

n = int(input())
d = input()
l_d = list(map(int, input().split()))

p_R = int(1e10)
p_L = int(1e10)
m_t = int(1e10)

for i in range(n):
    if d[i] == "R":
        p_R = i
    if d[i] == "L":
        p_L = i
    
    if p_R != 1e10 and p_L != 1e10:
        if p_L > p_R:
            m_t = min(m_t, (l_d[p_L] - l_d[p_R]) // 2)
    
print(-1 if m_t == 1e10 else m_t)