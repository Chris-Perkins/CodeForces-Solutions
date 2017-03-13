# Description of the problem can be found at http://codeforces.com/problemset/problem/577/A

n, x = map(int, input().split())
s = 0

for i in range(1, n + 1):
    if x % i == 0 and x // i <= n:
        s += 1

print(s)