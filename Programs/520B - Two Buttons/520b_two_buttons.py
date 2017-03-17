# Description of the problem can be found at http://codeforces.com/problemset/problem/520/B
n, w = map(int, input().split())
t = 0
while n != w:
    t += 1
    w += 1 if w < n or w&1 else -w//2
print(t)