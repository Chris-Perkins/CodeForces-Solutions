# Description of the problem can be found at http://codeforces.com/problemset/problem/350/A

_, _ = map(int, input().split())

l_g = list(map(int, input().split()))
l_b = list(map(int, input().split()))
m = min(l_g) * 2

for g in l_g:
    m = max(m, g)

for b in l_b:
    if b <= m:
        print(-1)
        quit()
print(m)