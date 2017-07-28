# Description of the problem can be found at http://codeforces.com/problemset/problem/820/A

c, v0, v1, a, l = map(int, input().split())

m_r = v1 - l
t = 1
c_r = v0 - l
c_p = min(v0, v1)
while c_p < c:
    c_r = min(m_r, c_r + a)
    c_p = max(0, c_p + c_r)
    t += 1
print(t)