# Description of the problem can be found at http://codeforces.com/problemset/problem/478/B

n, m = map(int, input().split())
x = n - m + 1
r = n % m
a = (m - r) * ((n // m) * (n // m - 1)) // 2 + r * ((n // m + 1) * (n // m)) // 2
print(a, (x * (x - 1)) // 2)