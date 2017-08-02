# Description of the problem can be found at http://codeforces.com/problemset/problem/387/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()

l = -1
t = 0
for ax in a:
    l += 1
    while l < len(b) and ax > b[l]:
        l += 1
    if l < len(b) and ax <= b[l]:
        t += 1
print(len(a) - t)