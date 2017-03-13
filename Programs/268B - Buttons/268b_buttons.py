# Description of the problem can be found at http://codeforces.com/problemset/problem/268/B

n = int(input())
s = 0
t = 0

while s < n:
    f = n - s - 1
    t += s*f + f
    s += 1

print(t + n)