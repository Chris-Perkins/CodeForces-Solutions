# Description of the problem can be found at http://codeforces.com/problemset/problem/435/A

n, m = map(int, input().split())
l_s = list(map(int, input().split()))

c_p = m
t = 0

for s in l_s:
    if c_p + s > m:
        t += 1
        c_p = s
    else:
        c_p += s
        
print(t)