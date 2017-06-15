# Description of the problem can be found at http://codeforces.com/problemset/problem/4/B

d, s_t = list(map(int, input().split()))

t_s = 0
l_h = list()
l_t = list()
for i in range(d):
    l_h.append(list(map(int, input().split())))
    
    s_t -= l_h[i][0]
    t_s += l_h[i][1] - l_h[i][0]
    
if s_t < 0:
    print("NO")
elif s_t <= t_s:
    print("YES")
    for h in l_h:
        print(h[0] + min(s_t, h[1] - h[0]), end = " ")
        s_t -= min(s_t, h[1] - h[0])
else:
    print("NO")