# Description of the problem can be found at http://codeforces.com/problemset/problem/439/A

n, d = map(int, input().split())
j = (n - 1) * 2
t = (n - 1) * 10
t += sum(list(map(int, input().split())))
if t > d:
    print("-1")
else:
    print(j + (d - t) // 5)