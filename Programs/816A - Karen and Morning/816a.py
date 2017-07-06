# Description of the problem can be found at http://codeforces.com/problemset/problem/816/A

h, m = input().split(":")

t = 0
while h[0] != m[1] or h[1] != m[0]:
    t += 1
    if int(m) == 59:
        h = ("0" if (int(h) + 1) % 24 < 10 else "") + "%d" % ((int(h) + 1) % 24)
    m = ("0" if (int(m) + 1) % 60 < 10 else "") + "%d" % ((int(m) + 1) % 60)

print(t)