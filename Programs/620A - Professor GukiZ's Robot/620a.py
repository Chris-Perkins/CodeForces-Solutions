# Description of the problem can be found at http://codeforces.com/problemset/problem/620/A

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

t = 0

print(max(abs(x2 - x1), abs(y2 - y1)))