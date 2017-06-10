# Description of the problem can be found at http://codeforces.com/problemset/problem/378/A

a, b = map(int, input().split())
w = 0
l = 0

for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        w += 1
    elif abs(a - i) > abs(b - i):
        l += 1
print("%d %d %d" % (w, 6 - w - l, l))