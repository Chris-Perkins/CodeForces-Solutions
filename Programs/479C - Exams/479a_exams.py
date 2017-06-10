# Description of the problem can be found at http://codeforces.com/problemset/problem/479/C

n = int(input())
s_s = set()
l_d = list()

for i in range(n):
    a, b = map(int, input().split())
    l_d.append([a, b])
    
l_d.sort()

m = 0
for d in l_d:
    if (m <= d[1]):
        m = d[1]
    else:
        m = d[0]
print(m)