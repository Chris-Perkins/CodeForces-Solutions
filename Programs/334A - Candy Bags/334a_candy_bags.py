# Description of the problem can be found at http://codeforces.com/problemset/problem/334/A

n = int(input())

a_n = [[0 for j in range(n)] for i in range(n)]

t = 1
for i in range(n):
    for j in range(n):
        a_n[i][j] = t
        t += 1

for i in range(n):
    o = 0
    for j in range(n):
        print(a_n[j][(i + o) % n], end = " ")
        o += 1
    print()