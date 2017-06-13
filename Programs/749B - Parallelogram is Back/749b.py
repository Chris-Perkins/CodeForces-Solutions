# Description of the problem can be found at http://codeforces.com/problemset/problem/749/B

x, y = map(int,input().split())
a, b = map(int,input().split())
c, d = map(int,input().split())
print(3)
print(a + x - c, b + y - d)
print(c + x - a, d + y - b)
print(c + a - x, b + d - y)