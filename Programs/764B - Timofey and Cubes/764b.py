# Description of the problem can be found at http://codeforces.com/problemset/problem/764/B

n = int(input())
l_c = input().split()

h = (n + 1) // 2 - 1

for i in range(n // 2):
    if i % 2 == 0:
        t = l_c[i]
        l_c[i] = l_c[n - i - 1]
        l_c[n - i - 1] = t

print(" ".join(l_c))