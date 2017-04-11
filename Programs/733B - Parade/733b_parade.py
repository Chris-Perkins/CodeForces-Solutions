# Description of the problem can be found at http://codeforces.com/problemset/problem/733/B

n = int(input())
t_l = 0
t_r = 0

m_l = 0
m_l_i = 0

m_r = 0
m_r_i = 0

a_n = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    l, r = map(int, input().split())
    t_l += l
    t_r += r
    a_n[i][0] = l
    a_n[i][1] = r


max_k = abs(t_l - t_r)
o = 0
for i in range(n):
    if abs(t_l - a_n[i][0] + a_n[i][1] - (t_r - a_n[i][1] + a_n[i][0])) > max_k:
        max_k = abs(t_l - a_n[i][0] + a_n[i][1] - (t_r - a_n[i][1] + a_n[i][0]))
        o = i + 1
    
print(o)