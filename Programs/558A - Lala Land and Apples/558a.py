# Description of the problem can be found at http://codeforces.com/problemset/problem/558/A

n = int(input())
l_l = list()
l_r = list()

t_l = 0
t_r = 0

for _ in range(n):
    x, a = map(int, input().split())
    
    if abs(x) // x != 1:
        t_l += 1
        l_l.append([x, a])
    else:
        t_r += 1
        l_r.append([x, a])

l_r.sort()
l_l.sort(reverse = True)

if t_l == t_r:
    s1 = sum(x[1] for x in l_l)
    s2 = sum(x[1] for x in l_r)
    print(s1 + s2)
elif t_l < t_r:
    s1 = sum(x[1] for x in l_l[:t_l])
    s2 = sum(x[1] for x in l_r[:t_l + 1])
    print(s1 + s2)
else:
    s1 = sum(x[1] for x in l_l[:t_r + 1])
    s2 = sum(x[1] for x in l_r[:t_r])
    print(s1 + s2)