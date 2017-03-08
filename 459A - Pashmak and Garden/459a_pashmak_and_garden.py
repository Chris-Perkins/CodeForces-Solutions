# Description of the problem can be found at http://codeforces.com/problemset/problem/459/A

x1, y1, x2, y2 = map(int, input().split())
d = max(abs(x1 - x2), abs(y1 - y2))
if d == 0:
    print("-1")
elif x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2):
    print("-1")
else:
    if x1 == x2:
        print("%d %d %d %d" % (x1 + d, y1, x2 + d, y2))
    elif y1 == y2:
        print("%d %d %d %d" % (x1, y1 + d, x2, y2 + d))
    elif (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
        print("%d %d %d %d" % (min(x1, x2), max(y1, y2), max(x1, x2), min(y1, y2)))
    else:
        print("%d %d %d %d" % (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))