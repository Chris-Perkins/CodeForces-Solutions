# Description of the problem can be found at http://codeforces.com/problemset/problem/432/B

n = int(input())

a = [0 for i in range(n)]
x = [0 for i in range(100001)]

for i in range(n):
    s, a[i] = map(int, input().split())
    x[s] += 1

for i in range(n):
    print(n - 1 + x[a[i]], n - 1 - x[a[i]])