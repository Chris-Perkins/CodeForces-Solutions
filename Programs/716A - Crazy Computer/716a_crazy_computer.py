# Description of the problem can be found at http://codeforces.com/problemset/problem/716/A

n, c = map(int, input().split())
l = list(map(int, input().split()))

p = l[n - 1]
s = 0

for i in range(n):
    if p - l[n - 1 - i] > c:
        print(s)
        quit()
    
    s += 1
    p = l[n - 1 - i]
print(s)