# Description of the problem can be found at http://codeforces.com/problemset/problem/538/B

n = int(input())

d_n = {}

t_n = n
m = 0
i = 0
while t_n > 0:
    i = max(1, i * 10)
    d_n[i] = t_n % 10
    t_n //= 10
    m = max(d_n[i], m)

print(m)
for _ in range(m):
    t_i = i
    o = 0
    while t_i > 0:
        o *= 10
        o += 1 if d_n[t_i] > 0 else 0
        d_n[t_i] -= 1
        t_i //= 10
    print(o, end = " ")