# Description of the problem can be found at http://codeforces.com/problemset/problem/166/A

n, k = map(int, input().split())

l_t = list([list(map(int, input().split())) for _ in range(n)])
l_t.sort(key=lambda x: (-x[0], x[1]))

l = 0
h = 0
t = 0

while k - l - 1 >= 0 and l_t[k - l - 1] == l_t[k - 1]:
    t += 1
    l += 1
while k + h < n and l_t[k + h] == l_t[k - 1]:
    t += 1
    h += 1

print(t)