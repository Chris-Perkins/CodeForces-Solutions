# Description of the problem can be found at http://codeforces.com/problemset/problem/583/B

n = int(input())
l_n = list(map(int, input().split()))
s_s = set()

r = 1
c = 0
i = 0
t = -1
while len(s_s) != n:
    if c not in s_s and i >= l_n[c]:
        i += 1
        s_s.add(c)
        
        if len(s_s) == n:
            break
    
    if c == 0:
        r = 1
        t += 1
    if c == n - 1:
        r = -1
        t += 1
        
    c += r

if n == 1:
    print(0)
else:
    print(t)