# Description of the problem can be found at http://codeforces.com/problemset/problem/124/A

n, a, b = map(int, input().split())
t = 0

f = False
for i in range(1, n + 1):
    if i - a - 1 >= 0 and n - i <= b:
        t += 1
        f = True
    elif f:
        break

print(t)