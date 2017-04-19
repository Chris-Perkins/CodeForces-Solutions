# Description of the problem can be found at http://codeforces.com/problemset/problem/682/A

def g_m(v):
    l_r = [0] * 5
    l_r[0] = v // 5
    for i in range(1, 5):
        l_r[i] = l_r[0] + (1 if v % 5 >= i else 0)
        
    return l_r

x, y = map(int, input().split())

l_mx = g_m(x)
l_my = g_m(y)

t = 0
for i in range(5):
    t += l_mx[i] * l_my[(5 - i) % 5]
    
print(t)