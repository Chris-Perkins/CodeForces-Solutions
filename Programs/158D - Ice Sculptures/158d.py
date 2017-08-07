# Description of the problem can be found at http://codeforces.com/problemset/problem/158/D

n = int(input())
t = list(map(int, input().split()))

v = sum(t)
for i in (x for x in range(3, n) if n % x == 0):
    for j in range(n // i):
        v = max(v, sum(t[j:: n // i]))

print(v)