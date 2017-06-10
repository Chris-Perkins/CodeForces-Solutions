# Description of the problem can be found at http://codeforces.com/problemset/problem/499/A

n, x = map(int, input().split())

t = 0
w = 0
for _ in range(n):
    l, r = map(int, input().split())
    w += (l - t - 1) - x * ((l - t - 1) // x)
    w += r - l + 1
    t = r
print(w)