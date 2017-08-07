# Description of the problem can be found at http://codeforces.com/problemset/problem/474/D

m = 1000000007
t, k = map(int, input().split())
a = [0] * 100001
a[:k] = [1] * k

for i in range(k, 100001):
    a[i] = (a[i - 1] + a[i - k]) % m
    
for i in range(1, 100001):
    a[i] = (a[i - 1] + a[i]) % m
    
for i in range(t):
    x, y = map(int, input().split())
    print((a[y] - a[x - 1]) % m)  