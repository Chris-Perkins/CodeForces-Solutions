# Description of the problem can be found at http://codeforces.com/problemset/problem/650/A

p = int(input())

d_x = {}
d_y = {}
d_t = {}

t = 0

for _ in range(p):
    x, y = map(int, input().split())
    if x in d_x:
        t += d_x[x]
        d_x[x] += 1
    else:
        d_x[x] = 1
    if y in d_y:
        t += d_y[y]
        d_y[y] += 1
    else:
        d_y[y] = 1
    
    s = ("%d,%d" % (x, y))
    if s in d_t:
        t -= d_t[s]
        d_t[s] += 1
    else:
        d_t[s] = 1

print(t)