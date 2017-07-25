# Description of the problem can be found at http://codeforces.com/problemset/problem/34/A

k = int(input())

m = 1001
l_s = list()
for n in list(map(int, input().split())):
    l_s.append(n)

m_i = list()
for i in range(0, k):
    if m > abs(l_s[i % k] - l_s[(i - 1) % k]):
        m = abs(l_s[i] - l_s[(i - 1) % k])
        m_i = list([i, (i - 1) % k])

print(" ".join(str(x + 1) for x in m_i))