# Description of the problem can be found at http://codeforces.com/problemset/problem/706/A

a, b = map(int, input().split())
m = 1e9
for _ in range(int(input())):
    x, y, v = map(int, input().split())
    m = min(m, (((x-a)**2 + (y-b)**2)**(1/2)) / v)

print(m)    