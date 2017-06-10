# Description of the problem can be found at http://codeforces.com/problemset/problem/581/B

n = int(input())
l_n = list(map(int, input().split()))

m = 0
l_a = [0 for i in range(n)]
for i in range(n):
    l_a[n - i - 1] = max(0, m + 1 - l_n[n - i - 1])
    m = max(m, l_n[n - i - 1])
print(" ".join(str(x) for x in l_a))