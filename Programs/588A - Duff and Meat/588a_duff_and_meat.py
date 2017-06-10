# Description of the problem can be found at http://codeforces.com/problemset/problem/588/A

n = int(input())
m = None
t = 0
for _ in range(n):
    w, c = map(int, input().split())
    if m == None or m > c:
        m = c
    t += m*w
print(t)