# Description of the problem can be found at http://codeforces.com/problemset/problem/454/B

n = int(input())

l_i = list(map(int, input().split()))

m_i = l_i.index(min(l_i))
p = l_i[m_i]

m_m = False
n_m_i = -1

for i in range(1, n):
    if not m_m and l_i[(m_i + i) % n] >= p:
        p = l_i[(m_i + i) % n]
    else:
        if l_i[(m_i + i) % n] == l_i[m_i]:
            if not m_m:
                m_m = True
                n_m_i = (m_i + i) % n
        else:
            print(-1)
            quit()

if n_m_i != -1:
    m_i = n_m_i

print((n - m_i) % n)