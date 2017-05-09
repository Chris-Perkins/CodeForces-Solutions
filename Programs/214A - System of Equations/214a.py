# Description of the problem can be found at http://codeforces.com/problemset/problem/214/A

n, m = map(int, input().split())

t = 0
for a in range(1001):
    for b in range(1001):
        if a**2 + b == n and a + b**2 == m:
            t += 1
        if a**2 + b > n or a + b**2 > m:
            break
print(t)