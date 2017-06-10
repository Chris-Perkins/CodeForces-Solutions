# Description of the problem can be found at http://codeforces.com/problemset/problem/574/A

n = int(input())
l_v = list(map(int, input().split()))

t = 0
while l_v[0] != max(l_v) or l_v.count(l_v[0]) > 1:
    m_i = 0
    m = l_v[0]
    for i in range(n - 1):
        if l_v[1 + i] >= m:
            m = l_v[1 + i]
            m_i = i + 1
    l_v[m_i] -= 1
    l_v[0] += 1
    t += 1
print(t)