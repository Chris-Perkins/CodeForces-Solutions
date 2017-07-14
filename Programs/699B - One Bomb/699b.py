# Description of the problem can be found at http://codeforces.com/problemset/problem/699/B

n, m = map(int, input().split())

l_w = list()
for _ in range(n):
    l_w.append(input())

h = [0] * m
v = [0] * n
w_c = 0

for i, s in enumerate(l_w):
    for j, c in enumerate(s):
        if c == "*":
            h[j] += 1
            v[i] += 1
            w_c += 1
    
for i in range(n):
    for j in range(m):
        if h[j] + v[i] - (l_w[i][j] == "*") == w_c:
            print("YES\n%d %d" % (i + 1, j + 1))
            exit()

print("NO")
        