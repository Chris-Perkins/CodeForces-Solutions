# Description of the problem can be found at http://codeforces.com/problemset/problem/259/B

g = []
o_s = 0
f_s = 0
p_s = 0
t_s = 0
for i in range(3):
    l = list(map(int, input().split()))
    s = sum(l)
    
    if i == 0:
        p_s = s
        f_s = s
    else:
        t_s += o_s + p_s - s
        o_s += p_s - s
        p_s = s
    g.append(l)

c_s = f_s + (f_s - t_s) // 2

for l_i in g:
    s = sum(l_i)
    a = list()
    for n in l_i:
        if n == 0:
            a.append(c_s - s)
        else:
            a.append(n)
    print(" ".join(str(x) for x in a))