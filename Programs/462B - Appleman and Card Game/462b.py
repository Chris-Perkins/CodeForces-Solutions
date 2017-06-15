# Description of the problem can be found at http://codeforces.com/problemset/problem/462/B

n, k = map(int, input().split())

a = [0] * 26
s = input()

for c in s:
    a[ord(c) - ord('A')] += 1

a.sort(reverse = True)

t = 0
i = 0

while k > 0:
    t += min(k, a[i]) ** 2
    k -= min(k, a[i])
    i += 1

print(t)