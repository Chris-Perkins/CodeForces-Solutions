# Description of the problem can be found at http://codeforces.com/problemset/problem/427/B

n, t, c = map(int, input().split())
l_p = list(map(int, input().split()))

t_c = 0
i = 0
c_l = 0
while i < n:
    if l_p[i] <= t:
        c_l += 1
    else:
        c_l = 0
    
    if c_l >= c:
        t_c += 1
    
    i += 1
    
print(t_c)