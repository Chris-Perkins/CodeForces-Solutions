# Description of the problem can be found at http://codeforces.com/problemset/problem/377/A

n, m, k = map(int, input().split())
t = [input().replace('.', 'X') for i in range(n)]
k = n * m - k - sum(i.count('#') for i in t)
t = [list(i) for i in t]
i, p = 0, []
while k:
    if 'X' in t[i]:
        j = t[i].index('X')
        t[i][j], p = '.', [(i, j)]
        k -= 1
        break
    i += 1

while k:
    x, y = p.pop()
    for i, j in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
        if i < 0 or j < 0: continue
        if i < n and j < m and t[i][j] == 'X':
            t[i][j] = '.'
            p.append((i, j))
            k -= 1
            if k == 0: break

for i in range(n): t[i] = ''.join(t[i])
print("\n".join(t))
