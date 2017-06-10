# Description of the problem can be found at http://codeforces.com/problemset/problem/38/A

n = int(input())
l_d = list(map(int, input().split()))
a, b = map(int, input().split())

a_s = [0] * (n + 1)
for i in range(len(l_d)):
    a_s[i + 1] = a_s[i] + l_d[i]

print(a_s[b - 1] - a_s[a - 1])