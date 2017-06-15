# Description of the problem can be found at http://codeforces.com/problemset/problem/629/B

n = int(input())

a_g = list([0] * 367 for _ in range(2))
a_b = [0] * 367

for _ in range(n):
    g, s, e = input().split()
    for i in range(int(s), int(e) + 1):
        a_g[1 if g == "F" else 0][i] += 1

m = 0
for i in range(1, 367):
    m = max(m, 2 * min(a_g[0][i], a_g[1][i]))
    
print(m)