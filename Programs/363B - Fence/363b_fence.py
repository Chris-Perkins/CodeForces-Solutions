# Description of the problem can be found at http://codeforces.com/problemset/problem/363/B

n, k = map(int, input().split())

l_h = list(map(int, input().split()))

s = [l_h[0]] + [0] * (n - 1)
for i in range(1, len(l_h)):
    s[i] = s[i - 1] + l_h[i]

m_h = None
m_i = 0
for i in range(n - k + 1):
    if not m_h:
        m_h = s[i + k - 1] - s[i] + l_h[i]
        m_i = i
    else:
        if m_h > s[i + k - 1] - s[i] + l_h[i]:
            m_h = s[i + k - 1] - s[i] + l_h[i]
            m_i = i

print(m_i + 1)        