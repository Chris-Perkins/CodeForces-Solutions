# Description of the problem can be found at http://codeforces.com/problemset/problem/702/A

n = int(input())
l_n = list(map(int, input().split()))

l = 1
m = 1
for i in range(1, n):
    if l_n[i] > l_n[i - 1]:
        l += 1
    else:
        l = 1
    m = max(l, m)
print(m)