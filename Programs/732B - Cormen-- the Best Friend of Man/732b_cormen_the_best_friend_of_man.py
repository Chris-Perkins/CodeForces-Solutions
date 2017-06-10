# Description of the problem can be found at http://codeforces.com/problemset/problem/732/B

n, k = map(int, input().split())
l_d = list(map(int, input().split()))
t = 0
for i in range(1, n):
    if l_d[i - 1] + l_d[i] < k:
        t += k - (l_d[i] + l_d[i - 1])
        l_d[i] += k - (l_d[i] + l_d[i - 1])
print(t)
for d in l_d:
    print("%d" % d, end = " ")