# Description of the problem can be found at http://codeforces.com/problemset/problem/507/B

r, x1, y1, x2, y2 = map(int, input().split())

d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

print(int(d // (2*r) + (1 if d % (2*r) != 0 else 0)))