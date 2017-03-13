# Description of the problem can be found on http://codeforces.com/problemset/problem/583/A

h_d = {}
v_d = {}

n = int(input())

for i in range(n * n):
    h, v = map(int, input().split())
    if h not in h_d and v not in v_d:
        print(i + 1, end = " ")
        h_d[h] = 1
        v_d[v] = 1