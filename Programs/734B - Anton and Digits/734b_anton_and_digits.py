# Description of the problem can be found at http://codeforces.com/problemset/problem/734/B

k2, k3, k5, k6 = map(int, input().split())

s = 256 * min(k2, k5, k6)
k2 -= min(k2, k5, k6)
s += 32 * min(k2, k3)

print(s)