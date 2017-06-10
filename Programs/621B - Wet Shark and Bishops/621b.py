# Description of the problem can be found at http://codeforces.com/problemset/problem/621/B

d_p = {}
d_s = {}

n_p = int(input())
t = 0

for i in range(n_p):
    x, y = map(int, input().split())
    if y != 1:
        d_n = 1 - y
        d = -(1 - y)
        s_n1 = x - d_n
        s_1 = x - d
        
        if s_n1 not in d_s:
            d_s[s_n1] = 0
        if s_1 not in d_p:
            d_p[s_1] = 0
        d_s[s_n1] += 1
        d_p[s_1] += 1
        
        t += d_s[s_n1] + d_p[s_1] - 2
    else:
        if x not in d_p:
            d_p[x] = 0
        if x not in d_s:
            d_s[x] = 0
        d_p[x] += 1
        d_s[x] += 1
        
        t += d_p[x] + d_s[x] - 2

print(t)