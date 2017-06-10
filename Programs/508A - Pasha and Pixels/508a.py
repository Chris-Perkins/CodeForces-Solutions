# Description of the problem can be found at http://codeforces.com/problemset/problem/508/A

n, m, k = map(int, input().split())

d_x = [0,  0, -1, -1]
d_y = [0, -1, 0,  -1]

a_p = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(k):
    y_o, x_o= map(int, input().split())
    a_p[y_o][x_o] = 1
    for j in range(4):
        y = y_o + d_y[j]
        x = x_o + d_x[j]
        if (x > 0 and y > 0) and (y + 1 <= n and x + 1 <= m) and a_p[y][x] + a_p[y][x + 1] + a_p[y + 1][x] + a_p[y + 1][x + 1] == 4:
            print(i + 1)
            quit()
print(0)