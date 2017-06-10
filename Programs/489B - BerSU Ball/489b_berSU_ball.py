# Description of the problem can be found at http://codeforces.com/problemset/problem/489/B

n = int(input())
l_b = list(map(int, input().split()))
l_b.sort()

m = int(input())
l_g = list(map(int, input().split()))
l_g.sort()

b_i = 0
g_i = 0
t = 0

while b_i < len(l_b) and g_i < len(l_g):
    if abs(l_b[b_i] - l_g[g_i]) <= 1:
        t += 1
        b_i += 1
        g_i += 1
    else:
        if l_b[b_i] < l_g[g_i]:
            b_i += 1
        else:
            g_i += 1

print(t)