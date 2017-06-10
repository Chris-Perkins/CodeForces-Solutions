# Description of the problem can be found at http://codeforces.com/problemset/problem/570/B

n, m = map(int, input().split())

if n - m > m - 1 and m + 1 <= n:
    print(m + 1)
elif m - 1 > 0:
    print(m - 1)
else:
    print(m)