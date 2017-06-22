# Description of the problem can be found at http://codeforces.com/problemset/problem/596/A

d_y = {}
d_x = {}

l_c = list()
l_c = list()

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    d_x[x] = 1
    d_y[y] = 1
    l_c.append([x, y])

if len(d_x) + len(d_y) < 4:
    print(-1)
    quit()

t_x = 0
t_y = 0
i = 1
for k_x in d_x:
    t_x += (-1 if i == 0 else 1) * k_x
    i = 0
i = 1
for k_y in d_y:
    t_y += (-1 if i == 0 else 1) * k_y
    i = 0

print(abs(t_x) * abs(t_y)) 
    
    