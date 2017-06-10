# Description of the problem can be found at http://codeforces.com/problemset/problem/34/B

n, m = map(int, input().split())
l_t = list(map(int, input().split()))
l_t.sort()

t_m = 0
c = 0
for t in l_t:
    if t < 0 and c < m:
        t_m -= t
        c += 1
    else:
        break

print(t_m)
