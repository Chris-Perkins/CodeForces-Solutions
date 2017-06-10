# Description of the problem can be found at http://codeforces.com/contest/782/problem/0

_ = input()

s_l = list(map(int, input().split()))
c_s = 0
m_s = -1
s_s = [0]*100002

for s in s_l:
    s_s[s] += 1
    
    if s_s[s] == 2:
        c_s -= 1    
    elif s_s[s] == 1:
        c_s += 1
        if c_s > m_s:
            m_s = c_s

print(m_s)