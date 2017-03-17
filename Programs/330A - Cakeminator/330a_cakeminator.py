# Description of the problem can be found at http://codeforces.com/problemset/problem/330/A

r, c = map(int, input().split())
s_r = set()
s_c = set()
t = 0
t_r = 0
for i in range(r):
    s = input()
    for j in range(c):
        if s[j] == "S":
            if i not in s_r:
                s_r.add(i)
                t_r += 1
            s_c.add(j)
            
for i in range(r):
    if i not in s_r:
        t += c

for j in range(c):
    if j not in s_c:
        t += t_r
        
print(t)
        