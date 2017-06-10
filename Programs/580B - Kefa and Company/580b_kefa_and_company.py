# Description of the problem can be found at http://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())

l_p = list()
for _ in range(n):
    l_p.append(list(map(int, input().split())))

l_p.sort()

l, h = 0, 0
f = 0
f_m = 0

while h < len(l_p):
    if l_p[h][0] - l_p[l][0] >= d:
        f -= l_p[l][1]
        l += 1
    else:
        f += l_p[h][1]
        h += 1
    
    f_m = max(f_m, f)

print(f_m)