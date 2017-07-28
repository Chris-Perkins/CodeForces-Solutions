# Description of the problem can be found at http://codeforces.com/problemset/problem/611/C

read = lambda: map(int, input().split())
h, w = read()
a = [input() for i in range(h)]
N = 501
vr = [[0] * N for i in range(N)]
hr = [[0] * N for i in range(N)]
for i in range(h):
    for j in range(w):
        vr[j + 1][i + 1] = vr[j][i + 1] + vr[j + 1][i] - vr[j][i]
        hr[j + 1][i + 1] = hr[j][i + 1] + hr[j + 1][i] - hr[j][i]
        if a[i][j] == '#': continue
        if i != h - 1 and a[i + 1][j] == '.': vr[j + 1][i + 1] += 1
        if j != w - 1 and a[i][j + 1] == '.': hr[j + 1][i + 1] += 1
q = int(input())
for i in range(q):
    r1, c1, r2, c2 = read()
    p1 = hr[c2 - 1][r2] - hr[c1 - 1][r2] - hr[c2 - 1][r1 - 1] + hr[c1 - 1][r1 - 1]
    p2 = vr[c2][r2 - 1] - vr[c1 - 1][r2 - 1] - vr[c2][r1 - 1] + vr[c1 - 1][r1 - 1]
    ans = p1 + p2
    print(ans)