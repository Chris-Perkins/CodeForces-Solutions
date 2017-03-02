# Description of the problem can be found at http://codeforces.com/problemset/problem/432/A

n, k = map(int, input().split())
l = list(map(int, input().split()))

s = 0
for i in range(n):
    if l[i] <= 5 - k:
        s += 1

print(s // 3)