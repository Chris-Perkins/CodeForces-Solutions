# Description of the problem can be found at http://codeforces.com/problemset/problem/275/A

l_l = list()

d_x = [ 0, -1,  1,  0,  0]
d_y = [-1,  0,  0,  1,  0]

for i in range(3):
    l_l.append(list(map(int, input().split())))

l_c = list(list(1 for _ in range(3)) for _ in range(3))

for i in range(3):
    for j in range(3):
        if l_l[i][j] % 2 == 1:
            for k in range(5):
                x = j + d_x[k]
                y = i + d_y[k]
                if y >= 0 and y < 3 and x >= 0 and x < 3:
                    l_c[y][x] = abs(1 - l_c[y][x])

for l in l_c:
    print("".join(str(i) for i in l))