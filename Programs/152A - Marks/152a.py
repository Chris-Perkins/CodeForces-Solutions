# Description of the problem can be found at http://codeforces.com/problemset/problem/152/A

n, m = map(int, input().split())
d_s = {}

l_s = list(set() for _ in range(m))

for i in range(n):
    s = input()
    
    for j in range(m):
        if j not in d_s:
            d_s[j] = int(s[j])
            l_s[j].add(i)
        elif d_s[j] < int(s[j]):
            d_s[j] = int(s[j])
            l_s[j].clear()
            l_s[j].add(i)
        elif d_s[j] == int(s[j]):
            l_s[j].add(i)

for i in range(1, m):
    l_s[0] = l_s[0].union(l_s[i])

print(len(l_s[0]))